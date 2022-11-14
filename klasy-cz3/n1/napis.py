class TestClass:
    napis: str

    def __init__(self) -> None:
        self.napis = ""

    def get_string(self) -> None:
        self.napis = input("Podaj napis")

    def print_string(self) -> None:
        print(self.napis)
