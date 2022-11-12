from builtins import abs


def main() -> None:
    # sprawdzenie przestrzeni nazwa
    print(dir(abs))
    # wyświetlenie dokumentacji
    print(abs.__doc__)
    # obliczenie wart, bewzglednej
    print(abs(-155))


if __name__ == "__main__":
    main()
