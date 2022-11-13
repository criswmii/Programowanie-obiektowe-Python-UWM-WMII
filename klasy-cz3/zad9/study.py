from typing import List


class Student:
    student_name: str
    marks: List[float]

    def __init__(self, student_name: str, marks: List[float]) -> None:
        self.student_name = student_name
        self.marks = marks
