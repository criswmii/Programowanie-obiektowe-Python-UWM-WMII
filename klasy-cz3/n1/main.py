from napis import TestClass


def main() -> None:
    napis1: TestClass = TestClass()
    napis1.get_string()
    napis1.print_string()


if __name__ == '__main__':
    main()
