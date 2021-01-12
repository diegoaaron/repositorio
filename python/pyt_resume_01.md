## Conceptos del paradigma de programación orientado a objetos

- **abstracción**: proceso mental en el cual extraemos las características esenciales de algo, ignorando los detalles superfluos.
- **encapsulación**: proceso en el cual se oculta el estado de las características de una abstracción y se permite su modificación solo por operaciones definidas en la abstracción. 
- **modularisación**: proceso de descomposición de un sistema en un conjunto de piezas cohesivas (con significado propio) y poco  acopladas (mínima interdependencia). 
- **jerarquización**: proceso de ordenar en niveles (jerarquias) los elementos (modulos) de un sistema.
  - *composición*: ocurre cuando un elemento (sistema) esta compuesto de otros (sistemas). Por ejemplo el sistema respiratorio esta compuestos de las fozas nasales, traquea y pulmones. Estos a su vez se compone de los albeolos, venas, etc. Este conepto explica la existencia de los conceptos de **clase** y **objeto**. 
  - *clasificación*: ocurre cuando un elemento (sistema) es la especialización de otro. Por ejemplo los animales pueden ser vertabrados o invertebrados,  dentro de los vertebrados tenemos a los reptiles, insectos y mamíferos. Dentro de los mamíferos a los perros, vacas, etc. Este concepto explica la existencia del concepto de **herencia**.

## Elementos del paradigma de programación orientado a objetos utilizando python

- **variable**: es un espacio en memoria que almace una valor.
- **función**: es un conjunto de código agrupado bajo un nombre y que puede ser invocado.
- **clase**: es un molde para crear objetos. La nomenclatura para el nombre de las clases compuestas utiliza la notación *CamelCase*.
  - *atributos*: son las características que tendran los objetos. Por ejemplo nombre, edad, etc.
  - *métodos*: son las funcionalidades que tendran los objetos. Por ejemplo *mostrar_nombre()*, *calcular_edad()*, etc. Un método es una *función* declarada dentro de una *clase* y por ende debe tener como primer *argumento* la palabra **self**. La ejecución de un método puede cambiar el estado de un objeto.
    - *método constructor*: es el primer método que entra en funcionamiento al instanciar un objeto.
- **objeto**: es la materialización de una clase. La acción de crear un objeto se denomina *instanciar*. 
  - *estado de un objeto*: es el conjunto de datos y objetos relacionados con un objeto en un momento dado. Un objeto puede tener múltiples estados a lo largo de su existencia. 

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

# Creación de un objeto (instanciación de la clase 'PerroPeruano')
primerPerro = PerroPeruano("sparky", "negro") 
# Mostrando un atributo del objeto creado
print("El perro se llama", primerPerro.nombre)
# Ejecutando un método del objeto creado 
primerPerro.avanzar()  
```

- **herencia**: mecanismo por el cual una clase (hija) hereda el código de otra clase (padre). Python soporta la herencia múltiple.

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

# Creación de un objeto (instanciación de la clase 'Persona')
primerEstudiante = Estudiante("Miguel", "Eliceo", 21) 
# Ejecutando un método heradado
primerEstudiante.saludar() 
# Ejecutando un método propio de la clase
primerEstudiante.mostrar_horario()
```

- **polimorfismo**: mecanismo que permite a diferentes clases, usar el mismo nombre para un método y este tenga comportamientos diferentes. 

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


# creación de un objeto (instanciación de la clase 'Persona')
primeraPersona = Persona("masculino", 30) 
# utilizando el método 'saludar()' de forma polimórfica 
primeraPersona.nacer() 
# creación de un objeto (instanciación de la clase 'Estudiante')
primerEstudiante = Estudiante("masculino", 30, "sanmarquino")
# utilizando el método 'saludar()' de forma polimórfica 
primerEstudiante.nacer() 
# creación de un objeto (instanciación de la clase 'Trabajador')
primerTrabajador = Trabajador("masculino", 30, "operario")
# utilizando el método 'saludar()' de forma polimórfica 
primerTrabajador.nacer()
```
