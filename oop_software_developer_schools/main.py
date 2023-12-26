from human import Human, HumanGender, SoftwareDeveloper
from programming_language import ProgrammingLanguage


def main():
    ivan = Human("Иван", HumanGender.male)
    ivan.introduce()

    anton = SoftwareDeveloper("Антон", HumanGender.male, ProgrammingLanguage("Python"))
    anton.introduce()


if __name__ == "__main__":
    main()
