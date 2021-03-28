# Tipos de datos

**listas**: tipo de dato que se puede ordenar, es mutable y permite elementos duplicados.

```python
mylist = ["banana","cherry", "apple"]

for i in mylist: # recorre la lista
    print(i)


if "Banana" in mylist: # valida si el elemento se encuentra
    print("yes")
else:
    print("no")


mylist.append("lemon") # agrega el elemento al final
print(mylist)


item = mylist.pop() # remueve el último elemento de la lista, lo asigna a la variable y retorna la lista
print(item)
print(mylist)


mylist = ["Banana","cherry", "apple"]
mylist.reverse() # invierte el orden de los valores en la lista
print(mylist)


mylist = [4, 3, 1, -1, -5, 10]
mylist.sort() # ordena los elementos de la lista
print(mylist)


list_org = ["banana", "cherry", "apple"]

list_cpy = list_org # forma erronea de copiar una lista
list_cpy2 = list_org.copy() # primera opción para copiar una lista
list_cpy3 = list(list_org) # segunda opción para copiar una lista
list_cpy4 = list_org[:] # tercera opción para copiar una lista

list_cpy.append("lemon")
list_cpy2.append("tuna")
list_cpy3.append("piña")
list_cpy4.append("azucar")

print(list_org)
print(list_cpy)
print(list_cpy2)
print(list_cpy3)
print(list_cpy4)


mylist = [1, 2, 3, 4, 5, 6]
b = [i*i for i in mylist] # creando lista a partir de otra
print(mylist)
print(b)

```

**tuplas**: tipo de dato que permite ser ordenado, es inmutable y permite elementos duplicados.

```python
# forma de declarar
mytuple = ("max", 4, "dos") 
mytuple2 = "max", 4, "dos"
mytuple3 = tuple(["Max", 28, "Boston"])


# descomponiendo una tupla en variables independientes
name, age, place = mytuple 
mytuple = (0, 1, 2, 3, 4)
i1, *i2, i3 = mytuple


# accediendo asus valores
item = mytuple[0]


# recorriendo y validando sus elementos
for i in mytuple:
    print(i)


if "Max" in mytuple:
    print("yes")
else:
    print("no")


mytuple = ('a', 'p', 'p', 'l', 'e')

print(mytuple.count('p')) # devuelve la cantidad de elementos
print(mytuple.index('e')) # retorna el índice del primer elemento encontrado

# slicing
a = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)

b = a[2:5]
c = a[::-1]

```

