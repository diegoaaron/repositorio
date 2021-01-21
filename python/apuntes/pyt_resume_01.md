## Elementos del paradigma de programación orientado a objetos

**variable**: es un espacio en memoria que almace una valor.

**función**: es un conjunto de código agrupado bajo un nombre y que puede ser invocado.

**clase**: es un molde para crear objetos. La nomenclatura para el nombre de las clases utiliza la notación *CamelCase*.
  - **atributos**: son las características que tendran los objetos. Por ejemplo nombre, edad, etc.
  - **métodos**: son las funcionalidades que tendran los objetos. Por ejemplo *mostrar_nombre()*, *calcular_edad()*, etc. Un método es una *función* declarada dentro de una *clase* y por ende debe tener como primer *parámetro* la palabra *self*. La ejecución de un método puede cambiar el estado de un objeto.
    - **método constructor**: es el primer método que entra en funcionamiento al instanciar un objeto.

**objeto**: es la materialización de una clase. La acción de crear un objeto se denomina *instanciar*. 
  - **estado de un objeto**: es el conjunto de datos y objetos relacionados con un objeto en un momento dado. Un objeto puede tener múltiples estados a lo largo de su existencia. 

```python
class PerroPeruano:

    def __init__(self, nombre, color): # método constructor 
        self.nombre = nombre # atributo
        self.color = color

    def avanzar(self): # método 
        print("El perro", self.nombre, "está avanzando")

    def detenerse(self):
        texto = "El perro de color " + self.color + " se ha detenido"
        return texto
    
    def molestar(self, ruido):
        print("El perro esta haciendo", ruido)


primerPerro = PerroPeruano("sparky", "negro") # Creación de un objeto (instanciación de la clase 'PerroPeruano')
print("El perro se llama", primerPerro.nombre) # Mostrando un atributo del objeto creado
primerPerro.avanzar() # Ejecutando un método del objeto creado 
```

**herencia**: mecanismo por el cual una clase (hija) hereda el código de otra clase (padre). Python soporta la herencia múltiple.

```python
class Persona:

    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido
    
    def saludar(self):
        print("Hola, mi nombre es", self.nombre)

class Estudiante(Persona):

    def __init__(self, nombre, apellido, grado_academico):
        super().__init__(nombre, apellido) # llamando al constructor de la clase padre 
        self.grado_academico = grado_academico 

    def mostrar_horario(self):
        print("Mi horario aun no esta definido")

primerEstudiante = Estudiante("Miguel", "Eliceo", 21) 
primerEstudiante.saludar() 
primerEstudiante.mostrar_horario()
```

**polimorfismo**: mecanismo que permite a diferentes clases, usar el mismo nombre para un método y este tenga comportamientos diferentes. 

```python
class Persona:

    def __init__(self, sexo, edad):
        self.sexo = sexo
        self.edad = edad

    def saludar(self):
        print("Una persona te saluda")

class Estudiante(Persona):

    def __init__(self, sexo, edad, grado_academico):
        super().__init__(sexo, edad)
        self.grado_academico = grado_academico

    def saludar(self):
        print("Una estudiante te saluda")
    
class Trabajador(Persona):

    def __init__(self, sexo, edad, cargo_laboral):
        super().__init__(sexo, edad)
        self.cargo_laboral = cargo_laboral

    def saludar(self):
        print("Una trabajador te saluda")

primeraPersona = Persona("masculino", 30) 
primeraPersona.saludar() 
primerEstudiante = Estudiante("masculino", 30, "sanmarquino")
primerEstudiante.saludar() 
primerTrabajador = Trabajador("masculino", 30, "operario")
primerTrabajador.saludar()
```
- [explicación complementaria 1](https://pythonpedia.com/es/tutorial/5100/polimorfismo)
- [explicación complementaria 2](https://youtu.be/Finb7JZJcWE?t=305)

