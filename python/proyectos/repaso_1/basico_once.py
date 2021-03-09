class Car:

    def company(self):
        print("Car belongs to Audi company")

    def model(self):
        print("The Model is R8.")

    def color(self):
        print("The color is silver")

class Bike:

    def company(self):
        print("Bike belongs to pulsar company")

    def model(self):
        print("The model is dominar")

    def color(self):
        print("The color is black")


def func(obj):
    obj.company()
    obj.model()
    obj.color()

car = Car()
bike = Bike()

func(car)
func(bike)

