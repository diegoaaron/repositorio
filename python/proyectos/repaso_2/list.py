# List: ordered, mutable, allows duplicate elements

mylist = ["Banana","cherry", "apple"]
print(mylist)

mylist2 = list()
print(mylist2)

mylist3 = [5, True, "apple", "apple"]
print(mylist3)

item = mylist[0]
print(item)

item2 = mylist[-1]
print(item2)

for i in mylist: # recorre una lista
    print(i)

if "Banana" in mylist: # valida un elmento en una lista
    print("yes")
else:
    print("no")

print(len(mylist)) # indica la cantidad de elementos

mylist.append("lemon") # agrega un elemento a la lista
print(mylist)

mylist.insert(1, "blueberry") # agrega un elemento en la posición indicada
print(mylist)

item = mylist.pop() # remueve el último elemento de la lista, lo asigna a la variable y retorna la lista
print(item)
print(mylist)

mylist.remove("cherry") # remueve el elemento de la lsita
print(mylist)

mylist.clear() # elimina todos los elementos de la lista
print(mylist)

mylist = ["Banana","cherry", "apple"]
mylist.reverse() # invierte el orden de los valores en la lista
print(mylist)


# se esta trabajando el resumen en  en pyt_resume_04