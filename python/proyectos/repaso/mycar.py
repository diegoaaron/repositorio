class Car:

    no_of_wheels = 4

    def __init__(self, model):
        self.model = model
        print("Hello I am the constructor method.")

    def brand(self):
        print("The brand is", self.model)

    def engine(self):
        print("Engine")

    def wheel(self):
        print("Wheel")


if __name__ == "__main__":
    toyota = Car("t0y0ta")
    toyota.brand()
    toyota.engine()
    toyota.wheel()

