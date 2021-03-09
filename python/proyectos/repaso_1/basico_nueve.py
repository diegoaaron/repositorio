class Vehicle:

    def __init__(self, brand_name, color):
        self.brand_name = brand_name
        self.color = color

    def get_brand_name(self):
        return self.brand_name


class Car(Vehicle):

    def __init__(self, brand_name, model, color):
        super().__init__(brand_name, color)
        self.model = model

    def get_description(self):
        return "Car name: " + self.get_brand_name() + self.model + " Color: " + self.color

c = Car("Audi", "r8", "Red")

print(c.get_description())
print(c.get_brand_name())

