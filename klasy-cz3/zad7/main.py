from study import Student


def main() -> None:
    print(type(Student))
    print(Student.__dict__)
    print(Student.__module__)


if __name__ == "__main__":
    main()
