class Car(object):
    model: str

    def __init__(self, model: str) -> None:
        self.model = model

    def drive(self) -> None:
        print("Drive!")
