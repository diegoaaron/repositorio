## Detalles sobre las funciones

**funcion**: es una pieza de software reutilizable.
- parametros: elementos definidos para introducir información en la función
- argumentos: información brindada a la función cuando es invocada.
- **return**: sentencia que permite retornar un valor al finalizar la ejecución de una función. Si no se indica, por defecto la función retorna *None*

```python
def suma(num1, num2): # 'num1' y 'num2' son parametros
    total = num1 + num2

    return total

print(suma(4,5)) # '4' y '5' son argumentos
```

**funciones con parametros por defecto**: el valor de los parametros son utilizados cuando al invocar la función no se definen argumentos para estos parámetros.

```python
def decir(mensaje, veces=1):
    print(mensaje * veces)

decir("hola",3)
decir("adios")
```

**comodin \*args**: permite que se agreguen argumentos ilimitados en una función los cuales se almacenan en una tupla bajo el nombre *args*. Se debe poner al final.

```python
def sumatoria(n, *args):
    print("n vale:", n)

    for a in args:
        print("item:", a)

sumatoria(10, 100, 200, 300)
```

**comodin \*\*kwargs**: permite que se agreguen argumentos ilimitados en la función los cuales se almacenan en un diccionario de nombre *kwargs*. Se debe poner al final.

```python
def calculos(n, **kwargs):
    print("n vale: ", n)

    for k,w in kwargs.items():
        print("llave:", k, "valor:", w)

calculos(10, primero=100, segundo=200, tercero=300)
```

**docstring**: característica que permite la documentación de una función de forma, utilizando las comillas triples.

```python
def print_max2(x, y):
    ''' Imprime el máximo numero entre 2 valores
        x: primer valor
        y: segundo valor

        Los números ingresados debe ser entero'''
    if x > y:
        return x
    elif y > x:
        return y
    else:
        return "empate"

print(print_max2.__doc__)
print(print_max2(50, 30))
print(print_max2(10, 20))
```