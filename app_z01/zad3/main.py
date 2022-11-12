from drink import SodaCan


def main() -> None:
    soda1: SodaCan = SodaCan(3.2, 5.3)
    print(soda1.get_volume())
    print(soda1.get_surface_area())


if __name__ == "__main__":
    main()
