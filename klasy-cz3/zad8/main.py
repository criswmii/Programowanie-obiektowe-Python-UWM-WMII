from study import Student
from mark import Marks


def main() -> None:
    student1: Student = Student()
    mark1: Marks = Marks()
    print(isinstance(student1, Student))
    print(isinstance(student1, Marks))
    print(isinstance(mark1, Marks))
    print(isinstance(student1, object))
    print(isinstance(mark1, object))
    print(issubclass(Marks, object))
    print(issubclass(object, Marks))
    print(issubclass(Student, object))


if __name__ == "__main__":
    main()
