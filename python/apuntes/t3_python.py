# Al utilizar números flotantes la letra 'E' significa 10 por lo cual el número 42.3E-4 es equivalente a 42.3*(10^-4)

# Las cadenas se pueden expresar en comillas simples dobles y triples. Las comillas triples preservan los saltos de línea 


# En Python 3.6 aparecen los 'f-strings' que permite crear cadenas con formatos. Son una forma simplificada de la función format() 

nombre = 'Rufo'
edad = 4

print(f"El perro {nombre} tiene {edad} años ;)")

# La función print() permite definir cambiar el salto de linea que tiene al final
print("esto es un ejemplo", end=' ')
print(" esto es otro ejemplo", end='xx')

# Dentro de las cadenas de texto existen las 'secuencias de escape' que permiten alterar el texto 

print("What's your name?") # La comilla simple se escapa siempre al estar dentro de una doble
print('What"s your name?') 

print("Podemos ver el \\ backslash") # utilizamos backslash para escapar caracteres y mostrarlos en consola
print("Esta linea \n se mostrara con un salto de linea") # utilizamos backslash para crear el salto de linea segun el lenguaje 'C'
print("Utilizando la tabulación \t por medio de escape de caracteres") 
print("Utilizando varias lineas \
para definir el texto a imprimir")

# Si se desea definir cadenas que no admitan ningun procesamiento (sin formato) como 'escape de caracteres' utilizamos el prefijo 'r' o 'R'
print(r"Esta es una cadena que no \n implementara el salto de linea defindo por medio del 'escape de caracteres'")
print(R"Esta es otra cadena que no \n implementara el salto de linea")

# Orden de prioridad de los operadores en Python. Los operadores se evaluan de izquierda a derecha 

# lambda : Lambda Expression
# if - else : Conditional expression
# or : Boolean OR
# and : Boolean AND
# not x : Boolean NOT
# in, not in, is, is not, <, <=, >, >=, !=, == : Comparisons, including membership tests and identity tests 
# | : Bitwise OR 
# ^ : Bitwise XOR 
# & : Bitwise AND 
# <<, >> : Shifts 
# +, - : Addition and subtraction 
# *, /, //, % : Multiplication, Division, Floor Division and Remainder 
# +x, -x, ~x : Positive, Negative, bitwise NOT 
# ** : Exponentiation 
# x[index], x[index:index], x(arguments...), x.attribute : Subscription, slicing, call, attribute reference 
# (expressions...), [expressions...], {key: value...}, {expressions...} : Binding or tuple display, list display, dictionary display, set display

# Dentro de Python existen 3 sentencias de control de flujo y son: if, for y while 

def controlflujoif(valor1, valor2):
    if valor1 == valor2:
        print("El {valor1} es igual al {valor2}".format(valor1 = valor1, valor2 = valor2))
    elif valor1 > valor2:
        print("El {valor1} es mayor al {valor2}".format(valor1 = valor1, valor2 = valor2))
    else:
        print("El {valor1} es menor al {valor2}".format(valor1 = valor1, valor2 = valor2))


controlflujoif(10,11)

def controlflujowhile(valor1, valor2):
    estado = True 
    contador = 0
    
    while estado:
        if valor1 > valor2:
            estado = False
        
        valor1 += 10 
        contador += 1

    print("El flujo realizo {0} iteraciones antes de terminar".format(contador))

controlflujowhile(11, 115)


def controlflujofor(inicio, fin):

    for i in range(inicio, fin):
        print(i)
    else:
        print("El loop ha terminado")

controlflujofor(10, 50)

# la sentencia 'break' sirve para detener las sentencias de control de flujo (if, for, while). Si esta sentencias tienen configurado una sentencia 'else' esta no se ejecutara si el 'break' se ejecuta. 

def pruebabreak():
    while True:

        s = input('Ingrese algo: ')
        
        if s == 'quit':
            break
        
        print(f"el texto {s} ingresado es incorrecto, su medida es", len(s), "sigue intentando")

# la sentencia 'continue' sirve para saltar el resto de las sentencias en una sentencia de control de flujo 

def pruebacontinue():
    while True:
        s = input("Ingrese algo: ")

        if s == 'quit':
            break

        if len(s) < 3:
            print("Muy pequeño")
            continue

        print("Lo ingresado es suficientemente larga")



# las funciones son piesas de programas reusables. Tenga en cuenta la terminología utilizada: los nombres dados en la definición de la función se denominan 'parámetros', mientras que los valores que proporciona en la llamada a la función se denominan 'argumentos'.

def print_max(a, b):
    if a > b:
        print(a, 'es mayor que', b)
    elif a == b:
        print(a, 'es igual que', b)
    else:
        print(a, 'es menor que', b)

print_max(3,4)

# las variables declaradas dentro de una función tienen como alcance solo la función

x = 50

def func(x):
    print('x is', x)
    x = 2
    print('Changed local x to', x)

func(x)
print('x is still', x)


# La sentencia 'global' permite declarar una variable que pueda ser accedida desde lo más amplia

x = 50

def func2():
    global x

    print('x is', x)
    x = 2 
    print('changed global x to', x)

func2()

print('value of x is', x)

# Dentro de las funciones se pueden definir parametros con valores fijos los cuales se utilizaran si al llamar a la función no se brinda ningun valor como argumento. Hay que tener en cuenta que los parametros con valores por defecto deben ir al final de la función ya que sino arrojaria error. Esto por que los valores se asignan a los parametros por posición. 

def say(message, time=1):
    print(message * time)

say('Hello')
say('World', 5)

# Tambien se puede dar valores a las funciones con argumentos de palabra clave. Esto consiste en pasar el nombre del parametro junto con el valor que desea sin respetar el orden en que se dio al parametro cuando se definio la función

def func3(a, b=5, c=10):
    print("a es", a, "b es", b, "c es ", c)

func3(3,7)
func3(25, c=24)
func3(c=50, a=100)

# Algunas veces uno puede desear definir una función que puede tomar cualquier número de parametros, esto se puede realizar utilizando el comodin *

def total(x=4, *args, **kwargs):
    print("x", x)

    for a in args:
        print("unico item:", a)
    
    for k,w in kwargs.items():
        print("llave:",k, "valor:", w)


total(5, 10,11,12,13, primero=20, segundo=21, tercero=23)

# La sentencia 'return' permite devolver un valor de la función y terminar su ejecución. Si se utiliza una función y esta no tienen ninguna sentencia de retorno de forma implicita la funcion retorna 'None'

def maximo(x, y):
    if x > y:
        return x
    elif y > x:
        return y
    else:
        return "empate"

maximo(10, 20)
maximo(888, 444)
maximo(333, 333)

# Las funciones cuentan con la característica 'Docstring' que permite la documentación de una función de forma sencilla.

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
