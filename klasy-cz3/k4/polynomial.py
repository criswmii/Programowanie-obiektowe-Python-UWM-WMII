from __future__ import annotations
from typing import List


class Polynomial:
    coefficients: List[int]

    def __init__(self, coefficients: List[int]) -> None:
        # uciecie zer na koniec listy
        while coefficients[-1] == 0:
            coefficients.pop()
            if len(coefficients) == 0:
                coefficients = [0]
                break

        self.coefficients = coefficients

    def deg(self) -> int:
        return len(self.coefficients) - 1

    def __str__(self) -> str:
        temp: str = ""
        n = len(self.coefficients)
        for i in range(n - 1, -1, -1):
            # pomiecie z wyswietlenia zer
            if self.coefficients[i] == 0:
                continue

            if i > 1:
                if self.coefficients[i] > 0:
                    temp += f"{self.coefficients[i]}*x^{i}+"
                else:
                    temp += f"({self.coefficients[i]})*x^{i}+"
            elif i == 1:
                if (self.coefficients[1]) > 0:
                    temp += f"{self.coefficients[1]}*x+"
                else:
                    temp += f"({self.coefficients[1]})*x+"
            else:
                if self.coefficients[0] > 0:
                    temp += f"{self.coefficients[0]}"
                else:
                    temp += f"({self.coefficients[0]})"

        # ustawienie wielomianu zerowego
        if temp == "":
            temp = "0"
        # usuniecie plusa z konca
        if temp[len(temp) - 1] == "+":
            temp = temp[:-1]
        return temp

    def __neg__(self) -> Polynomial:
        temp = [-x for x in self.coefficients]
        return Polynomial(temp)

    def __add__(self, other_poly: Polynomial) -> Polynomial:
        l1 = len(self.coefficients)
        l2 = len(other_poly.coefficients)
        self.coefficients += [0] * max((l2 - l1), 0)
        other_poly.coefficients += [0] * max((l1 - l2), 0)
        temp = [x + y for x, y in
                zip(self.coefficients, other_poly.coefficients)]
        return Polynomial(temp)

    def __sub__(self, other_poly: Polynomial) -> Polynomial:
        l1 = len(self.coefficients)
        l2 = len(other_poly.coefficients)
        self.coefficients += [0] * max((l2 - l1), 0)
        other_poly.coefficients += [0] * max((l1 - l2), 0)
        temp = [x - y for x, y in
                zip(self.coefficients, other_poly.coefficients)]
        return Polynomial(temp)

    def __mul__(self, other_poly: Polynomial) -> Polynomial:
        l1 = len(self.coefficients)
        l2 = len(other_poly.coefficients)
        temp = [0] * (l1 + l2 - 1)
        for i in range(l1):
            for j in range(l2):
                temp[i + j] += self.coefficients[i] * other_poly.coefficients[
                    j]

        return Polynomial(temp)

    # zmodyfikowana wersja by byla zgodna z mypy
    def __eq__(self, other_poly: object) -> bool:
        if not isinstance(other_poly, Polynomial):
            return NotImplemented

        return self.coefficients == other_poly.coefficients

    def __call__(self, x: int) -> int:
        temp = self.coefficients[0]
        for i in range(1, len(self.coefficients)):
            temp += self.coefficients[i] * x ** i

        return temp
