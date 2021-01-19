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

