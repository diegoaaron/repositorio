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

mytuple = ('a', 'p', 'p', 'l', 'e')

print(mytuple.count('p')) # devuelve la cantidad de elementos

print(mytuple.index('e')) # retorna el índice del primer elemento encontrado

mylist = list(mytuple)
mytuple2 = tuple(mylist)

print("lista: ", mylist, "mytuple:", mytuple2)

# slicing
a = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)

b = a[2:5]
c = a[::-1]

print(b)
print(c)

mytuple = "Max", 28, "Boston"
name, age, place = mytuple
print(name)
print(age)
print(place)

mytuple = (0, 1, 2, 3, 4)
i1, *i2, i3 = mytuple

print(i1)
print(i3)
print(i2)

import sys

mylist = [0, 1, 2, "hello", True]
mytuple = (0, 1, 2, "hello", True)

print(sys.getsizeof(mylist), "bytes")
print(sys.getsizeof(mytuple), "bytes")

import timeit

print(timeit.timeit(stmt="[0, 1, 2, 3, 4, 5]", number=1000000))
print(timeit.timeit(stmt="(0, 1, 2, 3, 4, 5)", number=1000000))


# se esta trabajando el resumen en  en pyt_resume_04