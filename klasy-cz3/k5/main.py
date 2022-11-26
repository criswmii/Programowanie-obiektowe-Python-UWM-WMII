from vector import Vector


def main() -> None:
    v1: Vector = Vector([1, 2, 3])
    print(v1)
    v2: Vector = Vector([-2, 4, -1])
    print(v1 + v2)
    print(v1 - v2)
    print(v1 * v2)
    v3: Vector = Vector([1, 2, 3])
    print(v1 == v2)
    print(v1 == v3)
    print(len(v1))
    v4: Vector = Vector([1, 2, 3, 4, -4, 2])
    print(len(v4))
    print(v4[1])
    print(v4[5])
    print(v3.norm())
    print(v1.inner(v2))


if __name__ == '__main__':
    main()
