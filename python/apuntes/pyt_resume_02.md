## Sentencias de control de flujo

**if - elif - else**: ejecuta un conjunto de instrucciones si se cumple la condicion.

```python
valor1 = 10
valor2 = 11

# forma 1

if valor1 == valor2:
    print(f"El {valor1} es igual al {valor2}")
elif valor1 > valor2:
    print(f"El {valor1} es mayor al {valor2}")
else:
    print(f"El {valor1} es menor al {valor2}")

# forma 2

num_a = 5
num_b = 4

if num_a > num_b: print(f"{num_a} is greater than {num_b}")
``` 

**while**: ejecuta un conjunto de instrucciones mientras la condicion sea verdad.

```python
# ejemplo 1

estado = True 
contador = 0
valor1 = 5

while estado:
    if valor1 > 10:
        estado = False
    
    valor1 += 1 
    contador += 1

print(f"El flujo realizo {contador} iteraciones antes de terminar")

# ejemplo 2

validador = True
num_a = 0

while validador:
    
    if num_a > 10:
        validador = False
        
    print(f" valor: {num_a}")
    num_a += 1

else:
    print("La secuencia ha finalizado")

``` 

**for**: ejecuta un conjunto de instrucciones dentro de un rango dado.

```python
# ejemplo 1

for i in range(0, 10):
    print(f"valor: {i}")

# ejemplo 2

for i in range (2, 9):
    print(f"valor: {i}")
else:
    print("El loop ha terminado")

``` 

**break**: detiene las sentencias de control de flujo (if, for, while). Si hay una sentencia *else* esta no se ejecutara si la sentencia *break* se ejecuta primero.

```python
while True:

    s = input('Ingrese algo: ')
    
    if s == 'quit':
        break
    else:
        print(f"el texto {s} ingresado es incorrecto, su medida es", len(s), "sigua intentando")
    
    contador += 1
    print(f"Intento: {contador}")
``` 

**continue**: sirve para saltar el resto de sentencias dentro de una sentencia de control de flujo. 

```python
while True:
    s = input("Ingrese algo: ")

    if len(s) < 3:
        print("texto pequeño - sentencia 'continue' ejecutada")
        continue

    print("sentencia 'continue' no ejecutada")

    if s == 'quit':
        print("adivino la palabra")
        break
``` 
