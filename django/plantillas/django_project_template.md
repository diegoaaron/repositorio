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
        │   │   └── magazine
        │   │       ├── migrations
        │   ├── settings
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