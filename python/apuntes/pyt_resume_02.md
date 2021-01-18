## Elementos del paradigma de programación orientado a objetos utilizando python (continuación)

- **encapsulación**: mecanismo que permite definir el grado de acceso y modificación de los atributos y métodos de una clase. En Python todos los atributos y métodos son públicos por lo cual no existe la **encapsulación**. Por otra parte si tiene la característica del **name mangling** que simulan en cierta forma este comportamiento.

- **clase abstracta**: mecanismo que permite definir clases y métodos que deben ser obligatoriamente implementados en sus clases hijas. Las clases abstractas no se instancia. Python utiliza el módulo *abc* para definir calses abstractas

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

## Particularidades de Python 

- name mangling: mecanismo de Python que ayuda a evitar las colisiones de nombres entre una clase padre e hija. Para esto se utiliza el _guion bajo_. Python indica utilizar _un guion bajo_ para señalar (a otros programadores) que un atributo o método es propio de la clase y no se debe ser usado en las clases hijas. Al utilizar  _dos guiones bajos_ el mecanismo de **name mangling** modficia el nombre del atributo o método a la forma `name_class.__name_atribute` para que no se sobreescriba el elento si es definido en una clase hija. 
  - [explicación complementaria 1](https://www.youtube.com/watch?v=ALZmCy2u0jQ)
  - [explicación complementaria 2](https://www.geeksforgeeks.org/name-mangling-in-python/)
  - [explicación complementaria 3](https://medium.com/analytics-vidhya/python-name-mangling-and-how-to-use-underscores-e67b529f744f) 

```python
# ejemplo pendiente
```

- dunder o magic methods: 