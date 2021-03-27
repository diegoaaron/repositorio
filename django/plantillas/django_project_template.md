## Estructura genérica de un proyecto Django

```shell
$~/Documentos/projectos_django/myproject_base/
.
├── env/
└── src/
    └── myproject_django/
        ├── myproject/
        │   ├── apps/
        │   │   └── core/ 
        │   │       ├── migrations/
        │   │       ├── static/
        │   │       │   └── core/
        │   │       │       ├── css/
        │   │       │       ├── img/
        │   │       │       └── js/
        │   │       ├── templates/
        │   │       │   └── core/
        │   │       │       ├── base.html
        │   │       │       └── index.html
        │   │       ├── __init__.py
        │   │       ├── admin.py
        │   │       ├── apps.py
        │   │       ├── models.py
        │   │       ├── tests.py
        │   │       ├── urls.py
        │   │       └── views.py
        │   ├── __init__.py
        │   ├── urls.py
        │   ├── settings.py
        │   ├── asgi.py
        │   └── wsgi.py 
        ├── manage.py
        ├── db.sqlite3
        └── requirements.txt
```