import enum


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
