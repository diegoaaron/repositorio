class Car:
    
    def __init__(self):
        self.brand_name = 'Audi'
        self.model = 'r8'
        self.__engine = '5.2 L v10'

    def get_description(self):
        return self.brand_name + self.model + " is the car"


if __name__ == "__main__":
    c = Car()
    print(c.get_description())
    print(c._Car__engine)