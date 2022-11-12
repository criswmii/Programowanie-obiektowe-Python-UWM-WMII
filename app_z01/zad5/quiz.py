class Student(object):
    first_name: str
    last_name: str
    total_score: int
    quiz_number: int

    def __init__(self, first_name: str, last_name: str, total_score: int,
                 quiz_number: int) -> None:
        self.first_name = first_name
        self.last_name = last_name
        self.total_score = total_score
        self.quiz_number = quiz_number

    def get_name(self) -> str:
        return self.first_name

    def add_quiz(self, score: int) -> None:
        self.total_score += score
        self.quiz_number += 1

    def get_total_score(self) -> int:
        return self.total_score

    def get_average_score(self) -> float:
        return self.total_score / self.quiz_number
