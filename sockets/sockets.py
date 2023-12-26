import socket
import select
from abc import ABC, abstractmethod
from typing import List
from config import PORT


class SocketDisconnected(Exception):
    ...


class SocketStrategy(ABC):
    @abstractmethod
    def handle_socket(self, socket, socket_list):
        ...


class NonBlockingSelectSocketStrategy(SocketStrategy):
    def handle_socket(
        self, main_sock: socket.socket, connections: List[socket.socket], buff_size: int
    ):
        print("Waiting")
        res, _, _ = select.select([main_sock, *connections], [], [])

        for sock in res:
            if sock is main_sock:
                self._accept_socket(sock, connections)
            else:
                try:
                    self._make_socket_response(sock, buff_size)
                except (ConnectionResetError, SocketDisconnected):
                    print(f"Socket {sock.getsockname()} disconnected")
                    connections.remove(sock)
                    sock.close()

    def _accept_socket(self, sock, connections):
        sock, addr = sock.accept()
        connections.append(sock)
        print(f"Accepted {addr}")

    def _make_socket_response(self, sock, buff_size):
        data = sock.recv(buff_size)
        decoded_data = data.decode("utf-8")

        if not decoded_data:
            raise SocketDisconnected

        print(f"Reveiced data: {decoded_data}")

        sock.send(data)
        print(f"Echoed data to socket {sock.getpeername()}")


class NonBlockingEpollSocketStrategy(SocketStrategy):
    def handle_socket(
        self, main_sock: socket.socket, connections: List[socket.socket], buff_size: int
    ):
        self.poll = select.epoll()

        self.poll.register(main_sock, select.EPOLLIN)

        while True:
            print("Waiting")
            res = self.poll.poll()

            for file_d, _ in res:
                print(f"New event from fd: {file_d}")
                if file_d == main_sock.fileno():
                    self._accept_socket(main_sock, connections)
                else:
                    sock = list(
                        filter(lambda s: s.fileno() == file_d, connections)
                    ).pop()
                    print(sock, sock.fileno())

                    try:
                        self._make_socket_response(sock, buff_size)
                    except (ConnectionResetError, SocketDisconnected):
                        print(f"Socket {sock.getsockname()} disconnected")
                        connections.remove(sock)
                        self.poll.unregister(sock)
                        sock.close()

    def _accept_socket(self, main_sock, connections):
        sock, addr = main_sock.accept()
        connections.append(sock)
        self.poll.register(sock, select.EPOLLIN)
        print(f"Accepted {addr}")

    def _make_socket_response(self, sock, buff_size):
        print(f"Trying to reveive from {sock.getpeername()}")
        data = sock.recv(buff_size)
        decoded_data = data.decode("utf-8")

        if not decoded_data:
            raise SocketDisconnected

        print(f"Reveiced data: {decoded_data}")

        sock.send(data)
        print(f"Echoed data to socket {sock.getpeername()}")


class Socket:
    def __init__(
        self,
        strategy: SocketStrategy,
        host="0.0.0.0",
        port=25565,
        is_blocking=True,
        buffer_size=1024,
    ) -> None:
        self.strategy = strategy
        self.host = host
        self.port = port
        self.buffer_size = buffer_size
        self._connections = []

        self._sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        if not is_blocking:
            self._sock.setblocking(False)

        self._sock.bind((self.host, self.port))
        self._sock.listen()

    def loop(self):
        print(f"Listening on {self.host}:{self.port}")

        while True:
            self.strategy.handle_socket(self._sock, self._connections, self.buffer_size)


def main():
    sock = Socket(NonBlockingSelectSocketStrategy(), is_blocking=False, port=PORT)

    sock.loop()


if __name__ == "__main__":
    main()
