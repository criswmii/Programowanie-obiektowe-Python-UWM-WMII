from __future__ import annotations


class Address:
    postalcode: str
    city: str
    house_number: int
    street: str
    suite: int

    def __init__(self, postalcode: str, city: str, house_number: int,
                 street: str, suite: int = 0) -> None:
        self.postalcode = postalcode
        self.city = city
        self.house_number = house_number
        self.street = street
        self.suite = suite

    def show(self) -> None:
        print(f"Adres: {self.street} {self.house_number}", end="")
        if self.suite != 0:
            print(f" {self.suite}", end="")

        print()
        print(f"Kod i miasto: {self.postalcode} {self.city}")

    def comes_before(self, other: Address) -> bool:
        return self.postalcode < other.postalcode
