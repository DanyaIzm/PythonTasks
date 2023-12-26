from human import Human, SoftwareDeveloper
from programming_language import ProgrammingLanguage


class DeveloperSchool:
    def __init__(self, programming_language: ProgrammingLanguage) -> None:
        self._programming_language = programming_language
        self._number_of_courses = 0

    def teach(self, human: Human):
        self._number_of_courses += 1
        print(f"Был обучен {self._number_of_courses} студент")

        return SoftwareDeveloper(human.name, human.gender, self._programming_language)

    @property
    def number_of_courses(self):
        return self._number_of_courses
