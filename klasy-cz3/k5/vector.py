from __future__ import annotations
from typing import List
from math import sqrt


class Vector:
    coefficients: List[int]

    def __init__(self, coefficients: List[int]) -> None:
        self.coefficients = coefficients

    def __repr__(self) -> str:
        return f"{self.coefficients}"

    def __add__(self, other: Vector) -> Vector:
        if len(self.coefficients) != len(other.coefficients):
            raise AttributeError(
                "Wektory są różnej długości, więc nie można ich dodać")

        temp: List[int] = [x + y for x, y in
                           zip(self.coefficients, other.coefficients)]
        return Vector(temp)

    def __sub__(self, other: Vector) -> Vector:
        if len(self.coefficients) != len(other.coefficients):
            raise AttributeError(
                "Wektory są różnej długości, więc nie można ich odejmować")

        temp: List[int] = [x - y for x, y in
                           zip(self.coefficients, other.coefficients)]
        return Vector(temp)

    # mul zwraca iloczyn po współrzędnych
    def __mul__(self, other: Vector) -> Vector:
        if len(self.coefficients) != len(other.coefficients):
            raise AttributeError(
                "Wektory są różnej długości, więc nie można ich mnożyć")

        temp: List[int] = [x * y for x, y in
                           zip(self.coefficients, other.coefficients)]
        return Vector(temp)

    # zmodyfikowana wersja by byla zgodna z mypy
    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Vector):
            return NotImplemented

        return self.coefficients == other.coefficients

    def __len__(self) -> int:
        return len(self.coefficients)

    # numeracja od 1 do n
    def __getitem__(self, item: int) -> float:
        if 1 <= item <= len(self.coefficients):
            return self.coefficients[item - 1]

        raise AttributeError("Błędy indeks współrzędnej")

    def __str__(self) -> str:
        return f"{self.coefficients}"

    # norma euklidesowa
    def norm(self) -> float:
        return sqrt(sum([x * x for x in self.coefficients]))

    def inner(self, other: Vector) -> float:
        if len(self.coefficients) != len(other.coefficients):
            raise AttributeError(
                "Wektory są różnej długości,"
                "więc policzyć iloczynu skalarnego")

        return sum(
            [x * y for x, y in zip(self.coefficients, other.coefficients)])
