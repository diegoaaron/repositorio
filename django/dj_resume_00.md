## Comandos 

#### instalación de pip
`sudo apt install python3-pip` 

#### instalación de virtualenv
`sudo -H pip3 install virtualenv` 

#### creación de entorno virtual con virtualenv
`virtualenv nombre_entor_virtual` 

#### activación del entorno virtual
`source nombre_entor_virtual/bin/activate`

#### desactivar el entorno virtual
`deactivate`

#### listar paquetes instalados con pip
`pip list`

#### instalar django
`pip install Django`
`pip install Django==3.1.1`

#### crear una lista de los programas instalados (para futuros despliegues de la aplicación)
`pip freeze > requirements.txt`

#### instalar una lista de programas desde un archivo
`pip install -r requirements.txt` 

#### instalar pylint (validador de código Python según la norma PEP8)
`pip install pylint`

#### crear un proyecto Django
`django-admin startproject name_project` 

#### ejecutar prueba de Django
`python manage runserver`

#### agregando una aplicación dentro de un proyecto
`python manage.py startapp name_app`

#### aplica los cambios de las migraciones en la base de datos
`python manage.py migrate`

#### crear un registro de los cambios que se desean guardar para una futura edición
`python manage.py makemigrations app_name`

#### mostrar los cambios que se desean guardar en formato SQL
`python manage.py sqlmigrate app_name 000X` 

#### validar si hay errores en las migraciones a aplicar en la base de datos
`python manage.py check`

#### ingresar al API de Django
`python manage.py shell`

#### creando usuario administrador del panel de administración de Django
`python manage.py createsuperuser`

#### empaquetar los archivos css, js e imágenes para ser utilizados
`python manage.py collectstatic`

#### ejecutar test automático a una aplicación
`python manage.py test app_name`



## Estructura de desarrollo

primero debo de acomodar toda las plantillas en la aplicación **base**

- creamos la aplicación
- agregamos la aplicación al proyecto (settings.py)
- agregamos la ruta de url de la aplicación al proyecto (urls.py)



##### Configuración de formularios y email

              cliente: 6Lficx0aAAAAAEPArYEX6Gb0kdRsTTDy0_Fo4fKD
              servidor: 6Lficx0aAAAAABJoFtIC5Iy-0rTejiuF8fcLMGwJ


##### Referencias

https://simpleisbetterthancomplex.com/tutorial/2017/02/21/how-to-add-recaptcha-to-django-site.html

https://simpleisbetterthancomplex.com/tips/2016/09/06/django-tip-14-messages-framework.html

##### Referencia



https://www.digitalocean.com/community/tutorials/how-to-install-and-use-postgresql-on-ubuntu-20-04-es

usuario creado diego

https://www.digitalocean.com/community/tutorials/how-to-deploy-django-to-app-platform



#### configuración

https://css-tricks.com/couple-takes-sticky-footer/



------------------------------------------------------------------------------------------------------------------------------------------------
Documentos y guías ya revisadas

# Instalación de virtualenv
https://virtualenv.pypa.io/en/stable/installation.html

# Documentación Django 3.1 (estructurada)
https://docs.djangoproject.com/en/3.1/

# Indice de las API de referencia de Django 3.1
https://docs.djangoproject.com/en/3.1/ref/

# Tutorial para desplegar una aplicación Django en Heroku
https://www.codementor.io/@jamesezechukwu/how-to-deploy-django-app-on-heroku-dtsee04d4
https://devcenter.heroku.com/articles/django-assets

# Configurar servidor ngnix + gunicorn para Django
https://www.digitalocean.com/community/tutorials/como-configurar-django-con-postgres-nginx-y-gunicorn-en-ubuntu-18-04-es

# Explicación de la diferencia entre ASGI y WSGI
https://www.maxongzb.com/why-asgi-is-replacing-wsgi-in-django-reading-time-3-mins/
https://medium.com/analytics-vidhya/difference-between-wsgi-and-asgi-807158ed1d4c

# 
