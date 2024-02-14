from developer_school import DeveloperSchool
from human import Human, SoftwareDeveloper


# [v] Паттерн "декоратор"
class DebugSchool:
    def __init__(self, developer_school: DeveloperSchool) -> None:
        # [v] Композиция объектов
        self._developer_school = developer_school

    def teach(self, human: Human) -> SoftwareDeveloper:
        human.introduce()
        human = self._developer_school.teach(human)
        human.introduce()

        return human

    @property
    def number_of_courses(self):
        return self._developer_school.number_of_courses
