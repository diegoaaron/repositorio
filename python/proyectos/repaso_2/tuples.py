# Tuple: ordenada, inmutable, permite elementos duplicados

mytuple = ("max", 4, "dos")
print(mytuple)

mytuple2 = "max", 4, "dos"
print(mytuple2)

mytuple3 = ("max",) # tupla de un solo elemento
print(mytuple3, "tipo:", type(mytuple3))

mytuple = tuple(["Max", 28, "Boston"])
print(mytuple)

item = mytuple[0]
item1 = mytuple[1]
item2 = mytuple[-1]
print("item:", item, "item1:", item1, "item2:", item2)

for i in mytuple:
    print(i)

if "Max" in mytuple:
    print("yes")
else:
    print("no")