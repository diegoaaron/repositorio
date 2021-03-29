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

from django.views.generic.base import RedirectView

urlpatterns = [
    ...
    path('auth/', include('bymecoffe.apps.core.urls', namespace='auth')), # agrega rutas de app interna
    path('', RedirectView.as_view(url='core/'), name='index'), # redirección por defecto a una app interna
]

```