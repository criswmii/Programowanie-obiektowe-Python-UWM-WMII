class Student:
    student_id: int
    student_name: str

    def __init__(self, student_id: int, student_name: str) -> None:
        self.student_id = student_id
        self.student_name = student_name
