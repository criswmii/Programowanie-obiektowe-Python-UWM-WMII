from shape import Shape


class Square(Shape):
    length: float

    def __init__(self, length: float) -> None:
        self.length = length

    def area(self) -> float:
        return self.length**2
