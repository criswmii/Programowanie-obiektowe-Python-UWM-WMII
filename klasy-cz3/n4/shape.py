from math import pi


class Circle:
    radius: float

    def __init__(self, radius: float) -> None:
        self.radius = radius

    def get_area(self) -> float:
        return pi * self.radius ** 2

    def get_perimeter(self) -> float:
        return 2 * pi * self.radius
