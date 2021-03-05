# Conceptos utilizados en los modelos

## Teoria de base de datos

- **entidad**: una entidad es una cosa u objeto del mundo real, también puede ser un concepto abstracto y es distinguible de todos los demás objetos. una entidad tiene un conjunto de propiedades o atributos que la caracterizan. Ejemplo: persona, auto, inscripción
  - **atributos**: son las características o propiedades de una entidad. Ejemplo: para la entidad *persona* sus atributos pueden ser dni, nombre, apellido, fecha de nacimiento y sexo.
  - **atributo principal**: es aquel atributo (o grupo de atributos) que permiten identificar de manera única a la entidad. Ejemplo: para la entidad *personal* su atributo principal sería *dni*
- **relación**: es una asociación entre diferentes entidades. Es un vínculo que nos permite definir una dependencia, es decir, nos permite exigir que varias entidades compartan ciertos atributos de forma indispensable.Ejemplo: para las entidades *Estudiante* y *Libro* dentro del contexto de una biblioteca, podríamos ver que hay una relación entre ambas, la cual llamaremos *Prestar*, dado que el *Estudiante* se presta *Libros* y analogamente estos *Libros* son prestados a *Estudiantes*.
- **cardinalidad**: indica la cantidad de elementos o instancias de una *Entidad A* que se relacionan con una instancia de una *Entidad B* y viceversa. Pueden ser de tres tipos (uno a uno, uno a muchos y muchos a muchos)
  - **uno a uno**: se da cuando un elemento de una *Entidad A* se relaciona unicamente con un solo elemento de una *Entidad B* y viceversa. Ejemplo: un elemento de la entidad *Profesor* se relaciona con un elmento de la entidad *Casillero*, a través de una relación denominada *Asignar* 
  - **uno a muchos**: se da cuando un elemento de una *Entidad A* se relaciona con cero o varios elementos de una *entidad B*, y cada elemento de la *entidad B* se relaciona unicamente con un elemento de la *entidad A*. Ejemplo: las entidades *País* y *Ciudad* tiene una relación denominada *Pertenecer* ya que a un país le pertenecen varias ciuidades y una ciudad pertenece solo a un país. 
  - **muchos a muchos**: se da cuando un registro de una *Entidad A* se relaciona con cero o varios registros de una *Entidad B*, y un registro de una *Entidad B* se relaciona con cero o varios registros de una *Entidad A*. Ejemplo: Entre las entidades "Estudiante" y "Libro" a través de una relación denominada "Prestamo" de muchos a muchos podemos decir que un *Estudiante* se presta muchos *Libros* y a la vez un *Libro* es prestado a muchos *Estudiantes*.
- **modelo entidad-relación**: es una forma de representar (herramienta) entidades relevantes de una base de datos asi como sus interrelaciones y propiedades. La representación se da a través de un diagrama con una simbología definida. 
  - **entidades**: se representan mediante un rectangulo y su nombre en el interior
  - **atributos**: se representan mediante un circulo, su nombre en el interior y van unidos con líneas a su respectiva entidad.
  - **relaciones**: se representan mediante un rombo, su nombre va en el interior y une una o más entidades
  - **cardinalidad**: se representa indicando el tipo de cardinalidad leida de extremo a extremo entre las entidades. Para esto, se toma un registro de una entidad y se observa con cuantos registros se puede relacionar como máximo en la otra entidad y viceversa.

![entidad y atributos](https://github.com/diegoaaron/repositorio/blob/main/django/apuntes/entidad_atributos.png)
![relación y cardinalidad](https://github.com/diegoaaron/repositorio/blob/main/django/apuntes/relacion_cardinalidad.png)