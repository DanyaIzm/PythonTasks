import socket
from config import PORT


def main():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    sock.connect(("localhost", PORT))

    while True:
        data = input("Enter smthg: ")
        encoded_data = data.encode("utf-8")

        sock.send(encoded_data)
        print("Sended!")

        data = sock.recv(1024)
        decoded_data = data.decode("utf-8")
        print(f"Received: {decoded_data}")


if __name__ == "__main__":
    main()
