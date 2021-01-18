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

