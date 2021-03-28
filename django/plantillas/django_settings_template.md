# Configuraciones de archivos

## settings.py

```python

INSTALLED_APPS = [
    ...
    'bymecoffe.apps.core', # agregar app interna
]

TIME_ZONE = 'America/Lima'  # zona horaria del proyecto

```

## urls.py 

```python

urlpatterns = [
    ...
    path('auth/', include('bymecoffe.apps.core.urls', namespace='auth')), # agregar rutas de app interna
]

```