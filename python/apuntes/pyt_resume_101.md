## Herramientas de consola

**f-strings**: a partir de Python 3.6 se pueden crear cadenas con formatos. Las cadenas se pueden expresar en comillas simples, dobles y triples(preservan los saltos de línea). Al utilizar números flotantes la letra 'E' representa al número 10 por lo cual el número 15E-4 es equivalente a 0.0015

```python
nombre = 'Rufo'
edad = 1

print(f"El perro {nombre} tiene {edad} años")
``` 

**input()**: función integrada que permite el ingreso de valores por consola

```python
nombre = input("Ingrese su nombre: ")

print(f"Su nombre es {nombre}")
``` 

**escape de caracteres**: el caracter backslash permite escapar caracteres usados por lenguaje. La comilla simple se escapa al estar entre comillas dobles y viceversa

```python
print("Podemos ver el \\ backslash")
print("Esta cadena \n se mostrara con un salto de linea") 
print("Utilizando la tabulación \t por medio de escape de caracteres") 
print("Utilizando varias lineas \
para definir el texto a imprimir")

print("What's your name?")
print('What"s your name?') 
``` 

**dir()**: función integrada que muestra los nombres que tiene definido un *módulo*, retornando una lista ordenada de cadenas.

```python
# Fibonacci numbers module

def fib(n):    # write Fibonacci series up to n
    a, b = 0, 1
    while a < n:
        print(a, end=' ')
        a, b = b, a+b
    print()

def fib2(n):   # return Fibonacci series up to n
    result = []
    a, b = 0, 1
    while a < n:
        result.append(a)
        a, b = b, a+b
    return result

>>> import fibo

>>> dir(fibo)
['__name__', 'fib', 'fib2']
```
> Si se utiliza sin parametros se mostrara una lista de todos los nombres definidos en el espacio de trabajo

```python
>>> a = [1, 2, 3, 4, 5]
>>> import fibo
>>> fib = fibo.fib
>>> dir()
['__builtins__', '__name__', 'a', 'fib', 'fibo', 'sys']
```

