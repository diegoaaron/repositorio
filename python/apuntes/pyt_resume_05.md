## Módulos y paquetes

**modulo**: es un archivo con extensión *.py* que almacena código Python. Este archivo puede poser variables, constantes, condiciones, funciones, clases, métodos etc...

```python
# modulo: user.py
class User():
    def __init__(self, username):
        self.username = username

    def hola(self):
        print (f"Hola {self.username}")
```

**paquetes** consiste en la agrupación de módulos dentro de una carpeta (directorio). Para considerarse un paquete, el directorio debe tener de forma adicional un archivo con el nombre *__init__.py* y ademas al menos un modulo.

```python
package/
    __init__.py
    archivo1.py
    archivo2.py
    archivo3.py
    subpackage/
        __init__.py
        submodulo.py
```

> El archivo __init__.py puede contener las importaciones de los modulos para facilitar el acceso a estos módulos desde el archivo que es llamado.

```python
# En el archivo package/__init__.py
from archivo1 import Archivo

# En tu programa que utiliza el paquete package
from package import Archivo
```

- [explicación complementaria 1](https://bitybyte.github.io/Organzando-codigo-Python/)
- [explicación complementaria 2](https://pywombat.com/articles/modulos-paquetes-python)

**__name__ == "__main__"**: todo modulo tiene un atributo especial llamado *__name__* que define el espacio de nombres en el que se está ejecutando. Es usado para identificar de forma única al módulo cuando es importado. Por otra parte *"__main__"* es el nombre del ámbito en el que se ejecuta el código de nivel superior (el programa principal)
> Es decir, si tienes un archivo llamado *mi_modulo.py*, si lo ejecutamos como programa principal el atributo *__name__* tendra el valor de *"__main__"*, si lo usamos importándolo desde otro módulo (import mi_modulo) el atributo *__name__* tendra el valor *mi_modulo*.

> Básicamente, lo que haces usando `if __name__ == “__main__”`: es ver si el módulo ha sido ejecutado directamente o no (importado). Si se ha ejecutado como programa principal se ejecuta el código dentro del condicional.

```python
# archivo mi_modulo.py

def hacer_algo():
    print("hola")

if __name__ == "__main__":
    hacer_algo()

# si ejecutamos este módulo con python mi_modulo.py, la función se ejecutara
```