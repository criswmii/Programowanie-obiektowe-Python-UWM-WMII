from shape import Circle


def main() -> None:
    circle1: Circle = Circle(3.2)
    print(type(circle1))
    print(type(circle1).__name__)
    print(circle1.__class__)
    print(circle1.__class__.__name__)


if __name__ == '__main__':
    main()
