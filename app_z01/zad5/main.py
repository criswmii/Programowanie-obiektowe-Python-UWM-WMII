from quiz import Student


def main() -> None:
    student1: Student = Student("John", "Smith", 200, 5)
    print(student1.get_name())
    student1.add_quiz(45)
    print(student1.get_total_score())
    print(student1.get_average_score())


if __name__ == "__main__":
    main()
