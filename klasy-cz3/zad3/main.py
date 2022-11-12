from auto import Car


def main() -> None:
    car1: Car = Car("Skoda Fabia")
    print(dir(car1))


if __name__ == "__main__":
    main()
