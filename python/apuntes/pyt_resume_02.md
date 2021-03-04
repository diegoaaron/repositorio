## Elementos del paradigma de programación orientado a objetos (continuación)

**encapsulación**: mecanismo que permite definir el grado de acceso y modificación de los atributos y métodos de una clase. En Python todos los atributos y métodos son públicos por lo cual no existe la *encapsulación*. Por otra parte si tiene una característica denominada *name mangling* que simulan en cierta forma este comportamiento.

- [explicación complementaria 1](https://stackoverflow.com/questions/62688315/private-attributes-in-python-and-pep8)
- [explicación complementaria 2](https://stackoverflow.com/questions/1641219/does-python-have-private-variables-in-classes)
- [explicación complementaria 3](https://stackoverflow.com/questions/64579610/how-does-the-concept-of-encapsulation-work-in-python?noredirect=1#comment114190784_64579610)
- [explicación complementaria 4](https://www.genbeta.com/desarrollo/cazadores-de-mitos-las-propiedades-privadas-en-python)

**método | atributo estático**: característica para un atributo o método de ser unicos en todos los objetos de la clase (no necesitan ser instanciados para ser accedidos). Los atributos de la clase que tienen asignado un valor se vuelven estáticas. Para definir un método como estático se utiliza el decorador *@staticmethod* 

```python
class Calculadora:
    pi = 3.14 # atributo estático

    @staticmethod
    def suma(a, b): # método de clase estático
        return a + b

    @staticmethod
    def multi(a, b):
        return a * b

    def mostrar_variables(self, a, b): # método de clase 
        print("a:", a, "b:", b)

print("La suma de 4 y 5 usando un método estatico es:", Calculadora.suma(4, 5))
primeracalculadora = Calculadora()
print("La suma de 5 y 6 es:", primeracalculadora.suma(5, 6))
```

- [explicación complementaria 1](https://blog.nearsoftjobs.com/tipos-de-m%C3%A9todos-en-python-cls-vs-self-d6da1e08efa8)

**clase abstracta**: mecanismo que permite definir clases y métodos que deben ser obligatoriamente implementados en sus clases hijas. Las clases abstractas no se instancian. Python utiliza el módulo *abc* para definir clases abstractas

```python
from abc import ABCMeta, abstractmethod

class Figura(metaclass=ABCMeta):
  @abstractmethod # decorador que define el método como abstracto
  def area(self):
    pass

  @abstractmethod
  def perimetro(self):
    pass

class Rectangulo(Figura):

  def __init__(self, ancho, altura):
    self.ancho = ancho
    self.altura = altura

  def area(self):
    return self.altura * self.ancho

  def perimetro(self):
    return 2 * (self.altura * self.ancho)

perimetroRectangulo = Rectangulo(3, 5)
print(perimetroRectangulo.area())
print(perimetroRectangulo.perimetro())
```

- [explicación complementaria 1](https://www.youtube.com/watch?v=H9SnCQvoNHk)
- [explicación complementaria 2](https://www.3engine.net/wp/2015/02/clases-abstractas-en-python/)