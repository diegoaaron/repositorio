# Teoria de base de datos

- **entidad**: una entidad es una cosa u objeto del mundo real, también puede ser un concepto abstracto y es distinguible de todos los demás objetos. una entidad tiene un conjunto de atributos (propiedades) que la caracterizan. Ejemplo: persona, auto, inscripción
  - **atributos**: son las características de una entidad. Ejemplo: en la entidad *Persona* sus atributos pueden ser dni, nombre, apellido.
  - **atributo principal**: es aquel atributo (o grupo de atributos) que permiten identificar de manera única a cada registro la entidad. Ejemplo: en la entidad *Persona* su atributo principal sería *dni*

- **relación**: es como se denomina la asociación de diferentes entidades.Ejemplo: para las entidades *Estudiante* y *Libro* dentro del contexto de una biblioteca, podríamos ver que hay una relación entre ambas, la cual llamaremos *Prestar*, dado que un *Estudiante* se presta *Libros* y analogamente un *Libro* es prestado a varios *Estudiantes*.

- **cardinalidad**: indica la cantidad de instancias de una *Entidad A* que se relacionan con una instancias de una *Entidad B* y viceversa. 
  - **uno a uno**: se da cuando una instancia de una *Entidad A* se relaciona unicamente con un solo instancia de una *Entidad B* y viceversa. Ejemplo: un elemento de la entidad *Profesor* se relaciona con un elemento de la entidad *Casillero*, a través de una relación denominada *Asignar* 
  - **uno a muchos**: se da cuando una instancia de una *Entidad A* se relaciona con cero o varias instancias de una *entidad B*, y cada instancia de la *entidad B* se relaciona unicamente con una instancia de la *entidad A*. Ejemplo: las entidades *País* y *Ciudad* tiene una relación denominada *Pertenecer* ya que a un país tiene varias ciuidades y una ciudad pertenece solo a un país. 
  - **muchos a muchos**: se da cuando una instancia de una *Entidad A* se relaciona con cero o varias instancias de una *Entidad B*, y una instancia de una *Entidad B* se relaciona con cero o varias instancias de una *Entidad A*. Ejemplo: las entidades "Estudiante" y "Libro" tienen una relación denominada "Prestamo" de muchos a muchos por lo cual podemos decir que un *Estudiante* se presta muchos *Libros* y a la vez un *Libro* es prestado a muchos *Estudiantes*.

- **modelo entidad-relación**: es una forma de representar (herramienta) entidades de una base de datos asi como sus atributos e interrelaciones. La representación se da a través de un diagrama con una simbología definida. 
  - **entidades**: se representan mediante un rectangulo y su nombre en el interior.
  - **atributos**: se representan mediante un circulo, su nombre en el interior y van unidos con líneas a su respectiva entidad.
  - **relaciones**: se representan mediante un rombo, su nombre va en el interior y une una o más entidades.
  - **cardinalidad**: se representa mediante una etiqueta en el exterior de la relación, respectivamente. Pueden ser "1:1", "1:N" y "N:M", indicando el tipo de cardinalidad leida de extremo a extremo entre las entidades. 

- **modelo relacional**: es la última fase del modelado de una base de datos relacional, en esta se realiza la representación de los elementos mencionados a través de tablas y guiandonos a partir del modelo relacional y un conjunto de reglas.
  - todas las tabla del modelo E-R se convierten en tablas en el modelo relacional
  - el atributo principal de cada entidad se le denominara *llave primaria* en el modelo relacional y se representara con las letras *PK - Primary Key* 
  - las relaciones entre dos entidades se representaran poniendo el atributo principal de una entidad como campo en la otra, se denominara *llave foranea* y se representara con las letras *"FK - Foreign Key"*, todo esto dependiendo el tipo de cardinalidad definido en el modelo E-R. 

[explicación complementaria 1](http://contenidos.sucerman.com/nivel2/web1/unidad2/leccion4.html)

> Representación gráfica de una Entidad y sus atributos

![entidad y atributos](https://github.com/diegoaaron/repositorio/blob/main/django/apuntes/img_000.png)

> Representación gráfica de Relación y Cardinalidad entre Entidades

![relación y cardinalidad](https://github.com/diegoaaron/repositorio/blob/main/django/apuntes/img_001.png)