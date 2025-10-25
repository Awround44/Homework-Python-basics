# Task 4
from abc import ABC, abstractmethod

class Person(ABC):

    def __init__(self, full_name: str, age: int):
        self.full_name = full_name
        self.age = age

    @abstractmethod
    def info(self) -> str:
        pass

    @abstractmethod
    def stipend(self) -> int:
        pass

    def compare_stipend(self, other: 'Person') -> str:
        if self.stipend() > other.stipend():
            return "larger"
        elif self.stipend() < other.stipend():
            return "smaller"
        return "equal"

class Student(Person):
    def __init__(self, full_name: str, age: int, group_number: str, average_grade: float):
        super().__init__(full_name, age)
        self.group_number = group_number
        self.average_grade = average_grade

    def info(self) -> str:
        return f"Student: {self.full_name}, Age: {self.age}, Group: {self.group_number}, Avg Grade: {self.average_grade}"

    def stipend(self) -> int:
        if self.average_grade == 5:
            return 6000
        elif self.average_grade < 5:
            return 4000
        return 0


class Aspirant(Student):
    def __init__(self, full_name: str, age: int, group_number: str, average_grade: float, thesis_title: str):
        super().__init__(full_name, age, group_number, average_grade)
        self.thesis_title = thesis_title

    def info(self) -> str:
        return f"Aspirant: {self.full_name}, Age: {self.age}, Group: {self.group_number}, Avg Grade: {self.average_grade}, Thesis: {self.thesis_title}"

    def stipend(self) -> int:
        if self.average_grade == 5:
            return 8000
        elif self.average_grade < 5:
            return 6000
        return 0

student = Student("Dimitry Volzok", 20, "Group1", 4.5)
aspirant = Aspirant("Jane Smith", 25, "Group2", 5.0, "Research")
print(student.info())
print(aspirant.info())
print(student.stipend())  # 4000
print(aspirant.stipend())  # 8000
print(student.compare_stipend(aspirant))  # smaller