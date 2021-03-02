class Vehicle:
    
    def __init__(self, name, color="silver"):
        self.name = name
        self.color = color

    def get_name(self):
        return self.name

    def get_color(self):
        return self.color

    

class Car(Vehicle):
    
    def get_color(self):
        self.color = 'black'
        return self.color

        

audi = Car("Auid", "r8")

print("The name of our car is ", audi.get_name(), " and the color is: ", audi.get_color())

