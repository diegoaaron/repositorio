## Particularidades de Python 

**name mangling**: mecanismo de Python que ayuda a evitar las colisiones de nombres entre una clase padre e hija. Para esto se utiliza el simbolo *guion bajo*. Python indica utilizar *un guion bajo* para señalar (a otros programadores) que el atributo o método es propio de la clase y no debe ser llamado directamente (sino utilizar getter y setter). Al utilizar  *dos guiones bajos* el mecanismo de name *mangling* modficia el nombre del atributo o método a la forma `name_class__name_atribute` para que no se sobreescriba el elemento si es definido en una clase hija.

```python
class Cuadrado:

    def __init__(self, length):
        self._side = length
        self._area = length**2
        self.__tipo = "figura geometrica"

    @property
    def area(self):
        return self._area

    @property
    def side(self):
        return self._side

    @property
    def tipo(self):
        return self.__tipo

    @side.setter
    def side(self, length):
        self._side = length
        self._reset_area()

    def _reset_area(self):
        self._area = self._side ** 2

miCuadrado = Cuadrado(10)
print("el lado es:", miCuadrado._side) # se puede porque '_' solo es una buena práctica mencionada en la PEP8
print("lado:", miCuadrado.side, "area:", miCuadrado.area) # forma correcta, utilizando getter
miCuadrado.side = 20 # forma correcta, utilizando el setter
print("lado actualizado: ", miCuadrado.side, "área actualizada: ", miCuadrado.area)

print("el cuadrado es de tipo:" miCuadrado.__tipo) # arroja error - name mangling modifico el nombre de la propiedad
print("el cuadrado es de tipo:", miCuadrado.tipo) # forma correcta, utilizando el getter
print("el cuadrado es de tipo:", miCuadrado._Cuadrado__tipo) # forma incorrecta, utilizando el nuevo nombre producido por el name mangling
```

- [explicación complementaria 1](https://www.youtube.com/watch?v=ALZmCy2u0jQ)
- [explicación complementaria 2](https://www.geeksforgeeks.org/name-mangling-in-python/)
- [explicación complementaria 3](https://medium.com/analytics-vidhya/python-name-mangling-and-how-to-use-underscores-e67b529f744f)
- [explicación complementaria 4](https://pythones.net/propiedades-en-python-oop/)

**dunder o magic methods**: es como se denomina a los métodos que inician y terminan con dos guiones bajo y permiten sobrecargar (personalizar) el comportamiento del objeto.

```python
class Friend:

    def __init__(self, name, age): # inicializa propiedades en las instancias de la clase
        self.name = name
        self.age = age

    def __str__(self): # muetra un mensaje cuando imprimimos un objeto de la clase de forma directa
        return f"{self.name} is {self.age} years old"

primerfriend = Friend("Eduard", 99)
print(primerfriend)
```

- [explicación complementaria 1](https://www.geeksforgeeks.org/dunder-magic-methods-python/)

