## Estructura genérica de un proyecto Django

```shell
$~/Documentos/django/myproject_website/
.
├── commands
├── db_backups
├── env
├── mockups
└── src
    └── django-myproject
        ├── externals
        │   ├── apps
        │   │   ├── cms
        │   │   ├── haystack
        │   │   └── storages
        │   └── libs
        │       ├── boto
        │       ├── requests
        │       └── twython
        ├── locale
        ├── media
        ├── myproject
        │   ├── apps
        │   │   ├── core
        │   │   │   ├── migrations
        │   │   │   └── __pycache__
        │   │   └── magazine
        │   │       ├── migrations
        │   │       │   └── __pycache__
        │   │       └── __pycache__
        │   ├── __pycache__
        │   ├── settings
        │   │   └── __pycache__
        │   ├── site_static
        │   │   └── site
        │   │       ├── css
        │   │       ├── img
        │   │       ├── js
        │   │       ├── scss
        │   │       └── vendor
        │   └── templates
        ├── requirements
        └── static

```