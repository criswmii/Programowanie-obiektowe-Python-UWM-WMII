class Rectangle:
    height: float
    width: float

    def __init__(self, height: float, width: float) -> None:
        self.height = height
        self.width = width

    def get_area(self) -> float:
        return self.height * self.width
