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

mylist = [4, 3, 1, -1, -5, 10]
mylist.sort() # ordena los elementos de la lista
print(mylist)

mylist = [4, 31, 1, -1, -5, 10]
new_list = sorted(mylist) # ordena los elementos de una lista
print(new_list)

mylist = [0] * 5 
print(mylist)

mylist2 = [1,2,3,4,5]

new_list = mylist + mylist2
print(new_list)

mylist = [1, 2, 3, 4, 5, 6, 7, 8, 9]

a = mylist[1:5]
b = mylist[1:]
c = mylist[::2]
d = mylist[::-1]

print(a)
print(b)
print(c)
print(d)

list_org = ["banana", "cherry", "apple"]

list_cpy = list_org
list_cpy2 = list_org.copy()
list_cpy3 = list(list_org)
list_cpy4 = list_org[:]

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
b = [i*i for i in mylist]
print(mylist)
print(b)

# se esta trabajando el resumen en  en pyt_resume_04