class Vehicle:

    def __init__(self, brand_name):
        self.brand_name = brand_name

    def get_brand_name(self):
        return self.brand_name

class Cost:

    def __init__(self, cost):
        self.cost = cost

    def get_cost(self):
        return self.cost

class Car(Vehicle, Cost):
    
    def __init__(self, brand_name, model, cost):
        Vehicle.__init__(self, brand_name)
        Cost.__init__(self, cost)
        self.model = model

    def get_description(self):
        return self.get_brand_name() + " " + self.model + " is the car " + "and it's cost" + self.get_cost()


c = Car("Audi", "r8", "2 cr")
print("Car description: ", c.get_description())

