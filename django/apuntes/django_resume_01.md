# Conceptos utilizados en los modelos

## Teoria de base de datos

- **entidad**: una entidad es una cosa u objeto del mundo real, también puede ser un concepto abstracto y es distinguible de todos los demás objetos. una entidad tiene un conjunto de propiedades o atributos que la caracterizan. Ejemplo: persona, auto, inscripción
  - **atributos**: son las características o propiedades de una entidad. Ejemplo: para la entidad *persona* sus atributos pueden ser dni, nombre, apellido, fecha de nacimiento y sexo.
  - **atributo principal**: es aquel atributo (o grupo de atributos) que permiten identificar de manera única a la entidad. Ejemplo: para la entidad *personal* su atributo principal sería *dni*
- **relación**: es una asociación entre diferentes entidades. Es un vínculo que nos permite definir una dependencia, es decir, nos permite exigir que varias entidades compartan ciertos atributos de forma indispensable.Ejemplo: para las entidades *Estudiante* y *Libro* dentro del contexto de una biblioteca, podríamos ver que hay una relación entre ambas, la cual llamaremos *Prestar*, dado que el *Estudiante* se presta *Libros* y analogamente estos *Libros* son prestados a *Estudiantes*.
  - **relación reflexiva**: se da cuando una entidad se relaciona consigo misma. Ejemplo: la entidad *Persona* es reflexiva a través de la relación *Trabajar*, ya que una persona puede trabajar para otra.
  - **relación binaria**: se da cuando hay una relación solo entre dos entidades. Ejemplo: la entidad Persona y Auto tienen una relación binaria a través de la relación Poseer.
  - **N-Aria**: Se da cuando en una misma relación intervienen más de 2 entidades. Ejemplo: la entidad Periodista, Artículo y Periodico las cuales se puede relacionar a través de la relación Escritura.
- **cardinalidad**: indica la cantidad de elementos o instancias de una *Entidad A* que se relacionan con una instancia de una *Entidad B* y viceversa. Pueden ser de tres tipos (uno a uno, uno a muchos y muchos a muchos)
  - **uno a uno**: se da cuando un elemento de una *Entidad A* se relaciona unicamente con un solo registro de una *Entidad B* y viceversa. Ejemplo: Una entidad *Profesor* y la entidad *Casillero*, con la relación *Asignar* 
  - **uno a muchos**: se da cuando un elemento de una Entidad A se relaciona con cero o varios registros de una entidad B, y cada registro de la entidad B se relaciona unicamente con un registro de la entidad A. Ejemplo: las entidades Pais y Ciudad tiene un relación de Pertenecer ya que varias ciudades pertenence a un pais y un pais tiene arias ciudadees 