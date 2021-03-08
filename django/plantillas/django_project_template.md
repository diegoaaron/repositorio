## Estructura genérica de un proyecto Django

```shell
$~/Documentos/django/myproject_base/
.
├── env/
├── mockups/
└── src/
    └── myproject_django/
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
        ├── myproject/
        │   ├── apps/
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