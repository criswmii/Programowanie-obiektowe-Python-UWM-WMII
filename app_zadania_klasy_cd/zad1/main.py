from ulamek import Wymierna


def main() -> None:
    wym1: Wymierna = Wymierna(3, 4)
    print("wym1", wym1)
    # wym2: Wymierna = Wymierna(3,0)
    wym3: Wymierna = Wymierna(9, 27)
    print("wym3", wym3)
    wym4: Wymierna = Wymierna(-9, 27)
    print("wym4", wym4)
    wym5: Wymierna = Wymierna(-9, -3)
    print("wym5", wym5)
    print(wym5.get_licznik())
    print(wym5.get_mianownik())
    print("wym4 float", float(wym4))
    wym6: Wymierna = Wymierna(1, 2)
    print("wym1+wym6", wym1 + wym6)
    print("wym1-wym6", wym1 - wym6)
    print("wym1==wym6", wym1 == wym6)
    print("wym1!=wym6", wym1 != wym6)
    print("wym1<wym6", wym1 < wym6)
    print("wym1<=wym6", wym1 <= wym6)
    print("wym1>wym6", wym1 > wym6)
    print("wym1>=wym6", wym1 >= wym6)


if __name__ == "__main__":
    main()
