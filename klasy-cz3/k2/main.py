from usa import American
from ny import NewYorker


def main() -> None:
    a1: American = American()
    print(a1.__class__)
    n1: NewYorker = NewYorker()
    print(n1.__class__)


if __name__ == "__main__":
    main()
