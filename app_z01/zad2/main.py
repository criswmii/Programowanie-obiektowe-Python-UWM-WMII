from adres import Address


def main() -> None:
    a1: Address = Address("10-710", "Olsztyn", 54, "Słoneczna")
    a1.show()
    a2: Address = Address("10-900", "Olsztyn", 15, "Tuwima", 5)
    print(a1.comes_before(a2))


if __name__ == "__main__":
    main()
