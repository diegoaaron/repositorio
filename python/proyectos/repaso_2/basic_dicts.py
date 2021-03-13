# Diccionario: estructura mutable, desordenada, que consiste en un par de valores clave valor.

mydict = {"name": "Max", "age": 28, "city": ""}
print(mydict)

mydict2 = dict(name="Mary", age=27, city="Boston")
print(mydict2)

value = mydict["name"]
print(value)

value2 = mydict2["age"]
print(value2)

mydict["email"] = "max@xyz.com" # agregando elemento
print(mydict)

mydict["email"] = "update_max@xyz.com" # actualizando elemento
print(mydict)

del mydict["name"] #eleminando clave valor
print(mydict)

mydict.pop("age") # elimina la clave valor
print(mydict)

mydict.popitem() # elimina la última clave-valor
print(mydict)

if "name" in mydict2: # buscando una llave
    print(mydict2["name"])

try:
    print(mydict2["lastname"])
except:
    print("Error")

for key in mydict2: # recorriendo diccionario - por defecto recorreo las llaves
    print(key)

for key in mydict2.keys(): # recorriendo llaves del diccionario
    print(key)

for value in mydict2.values(): # recorriendo valores del diccinario
    print(value)

for key, value in mydict2.items():
    print(key, value)

mydict3 = mydict2 # forma erronea de copiar una diccinario
mydict3["email"] = "abc@gmail.com" 
print(mydict2)
print(mydict3)

mydict4 = mydict2.copy() # forma correcta de copiado de un diccinario
mydict4["direccion 2"] = "algun lugar de la tierra"
print(mydict2)
print(mydict4)

mydict5 = dict(mydict2) # forma correcta de copiado 
mydict5["lugar"] = "sparky"
print(mydict2)
print(mydict5)

you_dict = {"name": "Max", "age": 28, "email": "max@gmail.com"}
you_dict2 = dict(name = "Mary", age = 28, city = "Boston")
you_dict.update(you_dict2)
print(you_dict)

mydict_f = {3: 9, 6: 36, 9: 81} # puede haber error al acceder a un valor por el índice 
print(mydict_f)

mytuple = (8, 7)
mydict_g = {mytuple: 15}
print(mydict_g)

