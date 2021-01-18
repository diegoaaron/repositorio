

# Atributo y método estático: característica para un atributo o método de ser unicos en todos los objetos de la clase (no necesitan ser instanciados para ser accedidos). Los atributos de la clase que tienen asignado un valor se vuelven estáticas. Para definir un método como estático se utiliza el decorador '@staticmethod' 

class Calculadora:
    pi = 3.14 # atributo de clase estático

    @staticmethod
    def suma(a, b): # método de clase estático
        return a + b

    @staticmethod
    def multi(a, b):
        return a * b

    def mostrar_variables(self, a, b): # método de clase 
        print("a:", a, "b:", b)

print("La suma de 4 y 5 usando un método estatico es:", Calculadora.suma(4, 5))
print("Mostrando una variable estática:", Calculadora.pi)
primeracalculadora = Calculadora()
print("La suma de 5 y 6 es:", primeracalculadora.suma(5, 6))






# Atributos de clase: son atributos comporatidos por todas las instancias de la clase

# Atributos de instancia: son atributos unicos para cada instancia de la clase

# el método isinstance() valida si un objeto es instancia de una clase y el método issubclass() valida si una clase hereda de otra

# crear un objeto a partir de una clase se denomina 'instanciar'

# estado: situación o modo de estar en un momento dado

# atributos: son las caraterísticas del objeto normalmente almacenadas en variables declaradas en la clase 

# metodos: son funciones que el objeto puede realizar y que a veces necesitan de ciertos argumentos para poder operar

# la práctica recomendad indica que se deben de crear métodos para modificar los atributos de nuestro objetos

