suma = lambda a: a + 10
print(suma(4))

squares = []
for x in range(10):
    squares.append(x**2)

print(squares)

squares2 = list(map(lambda x: x**2, range(10)))
print(squares2)

squares3 = list(x**2 for x in range(10))
print(squares3)

num_list = []
for i in range(10):
    for j in range(10):
        if i == j:
            num_list.append((i, j))


print(num_list)

num_list2 = list((i, j) for i in range(10) for j in range(10) if i == j)
print(num_list2)

class Car:
    def engine(self):
        print("Engine")

    def wheel(self):
        print("Wheel")

Car().engine()

toyota = Car()

