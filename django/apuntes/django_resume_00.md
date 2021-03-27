# Comandos de referencia

## Administración del entorno de trabajo

### actualizar pip3
`sudo pip3 install --upgrade pip setuptools wheel`

### crear un entorno virtual
`python3 -m venv env`

### activar el entorno virtual
`source env/bin/activate`

`. env_name/bin/activate`

### desactivar el entorno virtual
`deactivate`

### instalar Django  y Django Rest (dentro del entorno virtual)
```python
pip install Django  # instala la última versión del paquete
pip install "Django==3.1.5" # instala la versión especificada
pip install "Django~=3.0.0" # instala la versión más actual de la versión indicada
pip install djangorestframework 
```

### crear un proyecto Django
`django-admin.py startproject myproject`

### instalar paquetes desde un archivo
`pip install -r requirements.txt`

### crear lista de paquetes utilizados en el proyecto
`pip freeze > requirements.txt`

### crear una app 
`python manage.py startapp firstApp`

`django-admin startapp firstApp` || permite crear la aplicación en sub directorios

### crear un usuario de administración
`python manage.py createsuperuser`

### levantar el proyecto
`python manage.py runserver`

### interactuar por consola con Django
`python manage.py shell`

## Manipulación del modelo

### generar la estructura de migración para un modelo
`python manage.py makemigrations`

### mostrar las sentencias sql a implementar con la migración
`python manage.py sqlmigrate <app_name> <migration_name>` || example: `python manage.py sqlmigrate stores 0001` 

### valida si hay problemas en el proyecto relacionado a la migración a implementar
`python manage.py check`

### ejecuta las migraciones
`python manage.py migrate <app_name> <migration_name>` || example: `python manage.py migrate stores 0001`

`python manage.py migrate` || ejecuta todas las migraciones pendientes

### muestra el historico de migraciones (aplicadas o no) en el proyecto
`python manage.py showmigrations`


