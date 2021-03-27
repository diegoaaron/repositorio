## Estructura genérica de un proyecto Django

```shell
$~/Documentos/projectos_django/myproject_base/
.
├── env/
└── src/
    └── myproject_django/
        ├── media/???
        ├── myproject/
        │   ├── apps/
        │   │   ├── core/
        │   │   │   └── migrations/
        │   │   └── magazine/
        │   │       └── migrations/
        │   ├── settings.py
        │   ├── site_static/???
        │   │   └── site/
        │   │       ├── css/
        │   │       ├── img/
        │   │       ├── js/
        │   │       └── scss
        │   └── templates/???
        ├── manage.py
        ├── db.sqlite3
        ├── requirements.txt
        └── static/
```