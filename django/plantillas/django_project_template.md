## Estructura genérica de un proyecto Django

```shell
$~/Documentos/projectos_django/myproject_base/
.
├── env/
└── src/
    └── myproject_django/
        ├── media/ #por validar
        ├── myproject/
        │   ├── apps/ #agregar más componentes a las apps
        │   │   ├── core/ 
        │   │   │   └── migrations/
        │   │   └── magazine/
        │   │       └── migrations/
        │   ├── settings.py
        │   ├── site_static/ #por validar
        │   │   └── site/
        │   │       ├── css/
        │   │       ├── img/
        │   │       ├── js/
        │   │       └── scss
        │   └── templates/ #por validar
        ├── manage.py
        ├── db.sqlite3
        ├── requirements.txt
        └── static/
```