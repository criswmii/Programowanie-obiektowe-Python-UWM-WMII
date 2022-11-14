from shape import Circle


def main() -> None:
    circle1: Circle = Circle(3.2)
    print(circle1.get_perimeter())
    print(circle1.get_area())


if __name__ == '__main__':
    main()
