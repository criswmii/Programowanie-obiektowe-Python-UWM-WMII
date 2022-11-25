from polynomial import Polynomial


def main() -> None:
    p1: Polynomial = Polynomial([-1, -3])
    print(p1.deg())
    print(p1)
    mp1: Polynomial = -p1
    print(mp1)
    print(p1 + mp1)
    print(p1 + p1)
    p2: Polynomial = Polynomial([1, 2, 3, 4, 5])
    print(p1 + p2)
    print(p2 - p1)
    p3: Polynomial = Polynomial([3, 1])
    p4: Polynomial = Polynomial([2, 1])
    print(p3 * p4)
    p5: Polynomial = Polynomial([2, 1, 0, 0])
    print(p4 == p5)
    p6: Polynomial = Polynomial([6, 5, 1])
    print(p6 == p3 * p4)
    print(p6(1))
    print(p6(-1))
    print(p6(2))


if __name__ == "__main__":
    main()
