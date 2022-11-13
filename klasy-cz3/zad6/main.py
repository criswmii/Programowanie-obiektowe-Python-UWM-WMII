from study import Student


def main() -> None:
    student1: Student = Student()
    student1.student_data()
    student1.student_id = 123
    student1.student_data()
    student1.nazwa_ucznia = "Gosia"
    student1.student_data()
    student1.klasa_ucznia = "IIIc"
    student1.student_data()


if __name__ == "__main__":
    main()
