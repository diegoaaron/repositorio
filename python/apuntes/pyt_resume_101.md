## Herramientas de consola

**f-strings**: a partir de Python 3.6 se pueden crear cadenas con formatos. Las cadenas se pueden expresar en comillas simples, dobles y triples(preservan los saltos de línea). Al utilizar números flotantes la letra 'E' representa al número 10 por lo cual el número 15E-4 es equivalente a 0.0015

```python
nombre = 'Rufo'
edad = 1

print(f"El perro {nombre} tiene {edad} años")
``` 

**input()**: función que permite el ingreso de valores por consola

```python
nombre = input("Ingrese su nombre: ")

print(f"Su nombre es {nombre}")
``` 

**escape de caracteres**: El caracter backslash permite escapar caracteres usados por lenguaje. La comilla simple se escapa al estar entre comillas dobles y viceversa

```python
print("Podemos ver el \\ backslash")
print("Esta cadena \n se mostrara con un salto de linea") 
print("Utilizando la tabulación \t por medio de escape de caracteres") 
print("Utilizando varias lineas \
para definir el texto a imprimir")

print("What's your name?")
print('What"s your name?') 
``` 

