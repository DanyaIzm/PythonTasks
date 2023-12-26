from dataclasses import dataclass


@dataclass
class ProgrammingLanguage:
    name: str

    def __str__(self) -> str:
        return self.name
