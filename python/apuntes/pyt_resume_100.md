## Particularidades de Python 

**name mangling**: mecanismo de Python que ayuda a evitar las colisiones de nombres entre una clase padre e hija. Para esto se utiliza el *guion bajo*. Python indica utilizar *un guion bajo* para señalar (a otros programadores) que un atributo o método es propio de la clase y no debe ser usado en las clases hijas. Al utilizar  *dos guiones bajos* el mecanismo de name *mangling* modficia el nombre del atributo o método a la forma `name_class.__name_atribute` para que no se sobreescriba el elento si es definido en una clase hija.

  - [explicación complementaria 1](https://www.youtube.com/watch?v=ALZmCy2u0jQ)
  - [explicación complementaria 2](https://www.geeksforgeeks.org/name-mangling-in-python/)
  - [explicación complementaria 3](https://medium.com/analytics-vidhya/python-name-mangling-and-how-to-use-underscores-e67b529f744f) 

```python
# ejemplo pendiente
```

**dunder o magic methods**: es como se denomina a los métodos que inician y terminan con dos guiones bajo y permiten sobrecargar(personalizar) el comportamiento del objeto.

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

