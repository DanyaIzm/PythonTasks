from human import Human, HumanGender, SoftwareDeveloper
from programming_language import ProgrammingLanguage
from developer_school import DeveloperSchool


def main():
    ivan = Human("Иван", HumanGender.male)
    ivan.introduce()

    anton = SoftwareDeveloper("Антон", HumanGender.male, ProgrammingLanguage("Python"))
    anton.introduce()

    python_school = DeveloperSchool("Python")
    ivan = python_school.teach(ivan)
    ivan.introduce()


if __name__ == "__main__":
    main()
