# Tipos de datos

**listas**: tipo de dato que se puede ordenar, es mutable y soporta elementos duplicados.

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


item = mylist.pop() # elimina el último elemento de la lista, lo asigna a la variable y retorna la lista
print(item, mylist)


mylist = ["la","le", "li", "lo", "lu"]
del mylist[2] # elimina el elemento de la posición 2
print(mylist)


mylist = ["Banana","cherry", "apple"]
mylist.reverse() # invierte el orden de los valores en la lista
print(mylist)


mylist = [4, 3, 1, -1, -5, 10]
mylist.sort() # ordena los elementos de la lista
print(mylist)


list_org = ["banana", "cherry", "apple"]

list_cop = list_org # forma erronea de copiar una lista
list_cop.append("lemon")
print(list_org, list_cop) 

list_cop2 = list_org.copy() # primera opción para copiar una lista
list_cop2.append("tuna")
print(list_org, list_cop2)

list_cop3 = list(list_org) # segunda opción para copiar una lista
list_cop3.append("piña")
print(list_org, list_cop3)

list_cop4 = list_org[:] # tercera opción para copiar una lista
list_cop4.append("azucar")
print(list_org, list_cop4)


mylist = [1, 2, 3, 4, 5, 6]
new_list = [i*i for i in mylist] # creando lista a partir de otra
print(mylist, new_list)


mylist = ["la","le", "li", "lo", "lu"]
print(mylist[:]) # ["la","le", "li", "lo", "lu"]
print(mylist[:2]) # ['la', 'le']
print(mylist[2:]) # ['li', 'lo', 'lu']
print(mylist[1:3]) # ['le', 'li']
print(mylist[:-1]) # ['la', 'le', 'li', 'lo']
print(mylist[-1:]) # ['lu']


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

