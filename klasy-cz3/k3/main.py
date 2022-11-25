from shape import Shape
from square import Square


def main() -> None:
    s1: Shape = Shape()
    print(s1.area())
    s2: Square = Square(2.5)
    print(s2.area())


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()
