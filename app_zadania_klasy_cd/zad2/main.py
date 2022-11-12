from ulamek import Wymierna


def main() -> None:
    wym1: Wymierna = Wymierna(3, 4)
    wym2: Wymierna = Wymierna(1, 2)
    print("wym1*wym2", wym1 * wym2)
    print("wym1/wym2", wym1 / wym2)


if __name__ == "__main__":
    main()
