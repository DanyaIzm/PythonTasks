import enum

from programming_language import ProgrammingLanguage


class HumanGender(enum.Enum):
    male = "мужчина"
    female = "женщина"


# [v] Создание классов
class Human:
    def __init__(self, name: str, gender: HumanGender):
        self.name = name
        self.gender = gender

    def introduce(self) -> None:
        # [v] Форматирование строк
        print(f"Привет, я {self.gender.value}, меня зовут {self.name}.")


# [v] Наследование
class SoftwareDeveloper(Human):
    def __init__(
        self, name: str, gender: HumanGender, programming_language: ProgrammingLanguage
    ):
        # [v] Вызов родительских методов
        super().__init__(name, gender)
        self.programming_language = programming_language

    def introduce(self) -> None:
        print(
            f"Привет, я {self.gender.value}, меня зовут {self.name}. Я пишу на {self.programming_language}"
        )
