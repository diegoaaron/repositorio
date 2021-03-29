from django.urls import path, include

from django.contrib.auth import views as auth_views

from . import views

app_name = 'core'

urlpatterns = [
    path('', views.index, name = 'index'),
    path('login/', views.login, name = 'login'),
    path('logout/', auth_views.LogoutView.as_view(), name = 'logout'), # va
    path('social-auth', include('social_django.urls', namespace='social')), # va
]