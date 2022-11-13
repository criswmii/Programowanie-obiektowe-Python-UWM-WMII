from study import Student


def main() -> None:
    student1: Student = Student(123, "Kasia")
    print(student1.__dict__)
    student1.student_class = "IIIc"  # tego z typowaniem nie wiem jak zrobić
    print(student1.__dict__)
    del student1.student_name
    print(student1.__dict__)


if __name__ == "__main__":
    main()
