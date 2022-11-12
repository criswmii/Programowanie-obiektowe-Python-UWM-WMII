from __future__ import annotations
from math import gcd


class Wymierna(object):
    p: int
    q: int

    def __init__(self, licznik: int, mianownik: int) -> None:
        if mianownik == 0:
            raise ValueError("Mianownik nie może być równy zero.")

        self.p = licznik
        self.q = mianownik
        nwd: int = gcd(licznik, mianownik)
        if nwd != 1:
            self.p //= nwd
            self.q //= nwd

        if mianownik < 0:
            self.p *= (-1)
            self.q *= (-1)

    def __repr__(self) -> str:
        return f"{self.p}/{self.q}"

    def get_licznik(self) -> int:
        return self.p

    def get_mianownik(self) -> int:
        return self.q

    def __float__(self) -> float:
        return self.p / self.q

    def __add__(self, other: Wymierna) -> Wymierna:
        return Wymierna(self.p * other.q + self.q * other.p, self.q * other.q)

    def __sub__(self, other: Wymierna) -> Wymierna:
        return Wymierna(self.p * other.q - self.q * other.p, self.q * other.q)

    def __eq__(self, other: Wymierna) -> bool:
        return self.p == other.p and self.q == other.q

    def __ne__(self, other: Wymierna) -> bool:
        return self.p != other.p or self.q != other.q

    def __lt__(self, other: Wymierna) -> bool:
        return self.p * other.q < self.q * other.p

    def __le__(self, other: Wymierna) -> bool:
        return self.p * other.q <= self.q * other.p

    def __gt__(self, other: Wymierna) -> bool:
        return self.p * other.q > self.q * other.p

    def __ge__(self, other: Wymierna) -> bool:
        return self.p * other.q >= self.q * other.p

    def __mul__(self, other: Wymierna) -> Wymierna:
        return Wymierna(self.p * other.p, self.q * other.q)

    # brak __div__ w Pythonie 3
    def __truediv__(self, other: Wymierna) -> Wymierna:
        if other.p == 0:
            raise ValueError("Nie dziel przez zero!")
        return Wymierna(self.p * other.q, self.q * other.p)
