from study import Student


def main() -> None:
    student1: Student = Student("Ania", "IIb", 345)
    print(student1.nazwa_ucznia)
    print(student1.klasa_ucznia)
    print(student1.student_id)


if __name__ == "__main__":
    main()
