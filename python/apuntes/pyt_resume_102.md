## Sentencias de control de flujo

**if - elif - else**: ejecuta un conjunto de instrucciones si se cumple la condicion.

```python
def control_flujo_if(valor1, valor2):
    if valor1 == valor2:
        print(f"El {valor1} es igual al {valor2}")
    elif valor1 > valor2:
        print(f"El {valor1} es mayor al {valor2}")
    else:
        print(f"El {valor1} es menor al {valor2}")

control_flujo_if(10,11)
``` 

**while**: ejecuta un conjunto de instrucciones mientras la condicion sea verdad.

```python
def control_flujo_while(valor1, valor2):
    estado = True 
    contador = 0
    
    while estado:
        if valor1 > valor2:
            estado = False
        
        valor1 += 10 
        contador += 1

    print(f"El flujo realizo {contador} iteraciones antes de terminar")

control_flujo_while(11, 115)
``` 

**for**: ejecuta un conjunto de instrucciones dentro de un rango dado.

```python
def control_flujo_for(inicio, fin):

    for i in range(inicio, fin):
        print(i)
    else:
        print("El loop ha terminado")

control_flujo_for(10, 50)
``` 

**break**: sirve para detener las sentencias de control de flujo (if, for, while). Si hay una sentencia *else* esta no se ejecutara si la sentencia *break* se ejecuta primero.

```python
def prueba_break():
    while True:

        s = input('Ingrese algo: ')
        
        if s == 'quit':
            break
        
        print(f"el texto {s} ingresado es incorrecto, su medida es", len(s), "sigua intentando")

prueba_break()
``` 

**continue**: sirve para saltar el resto de sentencias dentro de una sentencia de control de flujo. 

```python
def pruebacontinue():
    while True:
        s = input("Ingrese algo: ")

        if len(s) < 3:
            print("Texto pequeño")
            continue

        print("sentencia 'continue' saltada")
        if s == 'quit':
            print("adivino la palabra")
            break

pruebacontinue()
``` 
