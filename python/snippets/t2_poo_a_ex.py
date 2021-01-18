
# Ejemplo de creación de una clase
class Piano:
    def __init__(self, color, num_patas, precio):
        self.color = color
        self.num_patas = num_patas
        self. precio = precio

    def tocar(self, musico):
        print("El músico ", musico, "esta tocando el piano")

    def mostrar_color(self):
        return self.color

    def mostrar_num_patas(self):
        return self.num_patas

    def mostrar_precio(self):
        return self.precio


primer_piano = Piano("negro", 4, 2500)

primer_piano.tocar("Diego")
primer_piano.mostrar_color()
print("color: ", primer_piano.mostrar_color())
print("n° patas: ", primer_piano.mostrar_num_patas())
print("precio: ", primer_piano.mostrar_precio())
print(primer_piano.color)
print(primer_piano.num_patas)
print(primer_piano.precio)
print("------------------")


# Ejemplo de herencia
class Poligono:
    def __init__(self, numero_lados):
        self.numero_lados = numero_lados

    def lados(self):
        print("Tengo", self.numero_lados, "lados")

class Triangulo(Poligono): 
    def __init__(self, numero_lados, tipo_triangulo):
        super().__init__(numero_lados)
        self.tipo_triangulo = tipo_triangulo

primerPoligono = Poligono(4)
primerPoligono.lados()
primerTriangulo = Triangulo(3, "equilatero")
primerTriangulo.lados()
print("------------------")


# Ejemplo de encapsulación 
class Juego:
    def __init__(self, nombre, creadores, year_publicacion):
        self.nombre = nombre
        self._creadores = creadores
        self.__year_publicacion = year_publicacion

    def jugar(self):
        print("Estoy jugando", self.nombre)

    def _creditos(self):
        print("El juego lo desarrollarón", self._creadores)


    def mostrando_atrib_privado(self):
        return self.__year_publicacion

class CrashCar(Juego):
    def __init__(self, nombre, creadores, year_publicacion, popularidad):
        super().__init__(nombre, creadores, year_publicacion)
        self.popularidad = popularidad

primerJuego = Juego("el juego", "diego, aaron", 2010)
primerCrashCar = CrashCar("Crash Rasing", "los mejores programadores", 2003, "muchisima")
print("la variable publica de 'primerJuego' es:", primerJuego.nombre)
print("la variable protegida de 'primerJuego' es:", primerJuego._creadores)
print("la variable privada de 'primerJuego' es:", primerJuego.mostrando_atrib_privado())

print("La variable protegida de 'primerJuego' accedida desde 'primerCrashCar es:", primerJuego._creadores)
print("la variable protegida de 'primerCrashCar' es:", primerCrashCar._creadores)

primerJuego.jugar()
primerCrashCar.jugar()
print("------------------")


# Ejemplo de clase abtracta
from abc import ABCMeta, abstractmethod

class Computadora(metaclass=ABCMeta):
    @abstractmethod
    def precio(self):
        pass

    def garantia(self):
        pass

class Laptop(Computadora):

    def __init__(self, marca, procesador, ram, disco):
        self.marca = marca
        self.procesador = procesador
        self.ram = ram
        self.disco = disco

    def precio(self, marca):
        if (self.marca == marca):
            return 1000
        else:
            return 1200

    def garantia(self, procesador, ram, disco):
        if (self.procesador == procesador and self.ram > ram and self.disco == disco):
            return 1
        else:
            return 2

primeralaptop = Laptop("acer", "intel", 4, 400)

print("el precio es: ", primeralaptop.precio("acer"))
print("la garantia es: ", primeralaptop.garantia("intel", 1, 1400))
print("------------------")


# Ejemplo de creación de una clase
class Dog:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def bark(self):
        print("bark bark!")

    def doginfo(self):
        print(self.name + " is " + str(self.age) + " year(s) old.")

    def birthday(self):
        self.age += 1

    def setBuddy(self, buddy): # una funcion puede soportar como atributo un objeto y modificarlo
        self.buddy = buddy
        buddy.buddy = self


ozzy = Dog("Ozzy", 2)
filou = Dog("Filou", 8)

ozzy.setBuddy(filou)

ozzy.buddy.doginfo()
filou.buddy.doginfo()
print("------------------")


# Ejemplo de una clase
class DogPull:
    """ Este es una clase sobre perros """ # cadena docstring

    species = "Canis familiaris" # atributo de clase

    def __init__(self, name, age): # metodo constructor
        self.name = name # atributo de instancia
        self.age = age

    def __str__(self):
        return f"{self.name} is {self.age} years old"

    def speak(self, sound): # método normal
        return f"{self.name} says {sound}"


primerperro = DogPull("rufo", 100)
segundoperro = DogPull("sparky", 3)
tercerperro = DogPull("toffy", 2)

print(segundoperro == tercerperro)

print(primerperro.species)
print(primerperro.name)
print(primerperro.age)

print(primerperro)
print(segundoperro.speak("bark bark!"))
print("------------------")


