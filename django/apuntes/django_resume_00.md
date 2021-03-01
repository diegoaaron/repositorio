## Comandos de referencia

#### actualizar pip3
`sudo pip3 install --upgrade pip setuptools wheel`

#### crear un entorno virtual
`python3 -m venv env`

#### activar el entorno virtual
`source env/bin/activate`
`. env_name/bin/activate`

#### desactivar el entorno virtual
`deactivate`

#### instalar Django (dentro del entorno virtual)
```python
pip install Django  # instala la última versión del paquete
pip install "Django==3.1.5" # instala la versión especificada
pip install "Django~=3.0.0" # instala la versión más actual de la versión indicada
```

#### crear un proyecto Django
`django-admin.py startproject myproject`

#### instalar paquetes desde un archivo
`pip install -r requirements/dev.txt`

#### crear lista de paquetes utilizados en el proyecto
`pip freeze > requirements/dev.txt`

#### crear una app 
`python manage.py startapp firstApp`

