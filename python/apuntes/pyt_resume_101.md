## Manipulación de cadenas

> Las cadenas se pueden expresar en comillas simples, dobles y triples(preservan los saltos de línea) 

> Al utilizar números flotantes la letra 'E' representa al número 10 por lo cual el número 15E-4 es equivalente a 0.0015

**f-strings**: a partir de Python 3.6 se pueden crear cadenas con formatos

```python
nombre = 'Rufo'
edad = 1

print(f"El perro {nombre} tiene {edad} años")
``` 

## Escape de caracteres

> La comilla simple se escapa al estar entre comillas dobles y viceversa

```python
print("What's your name?")
print('What"s your name?') 
``` 

> El caracter backslash permite escapar caracteres usados en el lenguaje y mostrarlos en consola

```python
print("Podemos ver el \\ backslash")
print("Esta linea \n se mostrara con un salto de linea") 
print("Utilizando la tabulación \t por medio de escape de caracteres") 
print("Utilizando varias lineas \
para definir el texto a imprimir")
``` 