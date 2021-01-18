# Recogiendo caramelos

# Krishna ama mucho los dulces, así que cuando los compra, los guarda para poder comerlos más tarde.
# Recientemente ha recibido N cajas de caramelos, cada una de las cuales contiene "Ci" caramelos, donde "Ci" representa el número de caramelos de la caja. Krishna quiere guardarlos en una sola caja. La única condición es que pueda elegir dos cajas cualesquiera y almacenar su contenido en una nueva caja vacía. Asumiendo que hay un número infinito de cajas vacias disponibles. 
# Se puede tomar dos cajas cualesquiera para transferir el contenido "X" e "Y" de caramelos respectivamente, tomandole  exactamente "X" + "Y" segundos de tiempo. Como está demasiado ansioso para recogerlos todos, se ha acercado a tí para para consultarte el tiempo mínimo en el que puede recoger todos los caramelos. 

# Formato de entrada:
# * La primera línea de entrada es el número de caso de prueba T
# * Cada caso de prueba se compone de dos entradas
# * La primera entrada de un caso de prueba es el número N de cajas
# * La segunda entrada son enteros delimitados por espacios en blanco que denotan el número de caramelos por cada caja.

# Formato de salida:
# * Mostrar el mínimo número de segundos requeridos para cada caso de prueba. Imprimir cada salida en una nueva línea. 

# Restricciones:
# 1 < T < 10
# 1 < N < 10000
# 1 < [Candies in cada caja] < 100009

def ejercicio_caramelos():
    T = int(input())
    arr = []
    arr0 = []
    arr1 = []
    for i in range(0, T):
        N = int(input())
        B = input()
        for i in B.split(" "):
            arr.append(int(i))
        for i in range(0, N):
            arr0.append(arr[i])
        print(arr0)
        arr0.sort()
        count = arr0[0]
        for i in range(1, len(arr0)):
            count = count + arr0[i]
            arr1.append(count)
    print(sum(arr1))

ejercicio_caramelos()
