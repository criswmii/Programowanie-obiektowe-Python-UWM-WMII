from study import Student


def main() -> None:
    student1: Student = Student("Ola", [4.5, 5.0, 3.5])
    print(student1.student_name)
    print(student1.marks)
    print(student1.__dict__)
    student1.student_name = "Olga"
    student1.marks = [2.0, 3.5, 4.0]
    print(student1.student_name)
    print(student1.marks)
    print(student1.__dict__)


if __name__ == "__main__":
    main()
