from human import Human, HumanGender, SoftwareDeveloper
from programming_language import ProgrammingLanguage
from developer_school import DeveloperSchool
from debug_school import DebugSchool


# [v] Утиная типизпция (в DeveloperSchool может попасть DebugSchool, ибо интерфейс один)
# [v] Совместимость объектов разных типов ^
def teach(human: Human, school: DeveloperSchool) -> SoftwareDeveloper:
    return school.teach(human)


def main():
    js_school = DeveloperSchool(ProgrammingLanguage("JavaScript"))
    python_school = DeveloperSchool(ProgrammingLanguage("Python"))

    js_debug_school = DebugSchool(js_school)
    python_debug_school = DebugSchool(python_school)

    ivan = Human("Иван", HumanGender.male)

    anton = SoftwareDeveloper("Антон", HumanGender.male, ProgrammingLanguage("Ruby"))

    ivan.introduce()
    ivan = teach(ivan, js_school)
    ivan.introduce()

    anton = teach(anton, js_debug_school)

    ivan = teach(ivan, python_debug_school)
    anton = teach(anton, python_debug_school)

    print(
        f"В Python Debug School обучились {python_debug_school.number_of_courses} раз"
    )
    print(
        f"В JavaScript Debug School обучились {js_debug_school.number_of_courses} раз"
    )
    print(f"В Python School обучились {python_school.number_of_courses} раз")
    print(f"В JavaScript School обучились {js_school.number_of_courses} раз")


if __name__ == "__main__":
    main()
