from shape import Rectangle


def main() -> None:
    rect1: Rectangle = Rectangle(3.4, 7.1)
    print(rect1.get_area())


if __name__ == '__main__':
    main()
