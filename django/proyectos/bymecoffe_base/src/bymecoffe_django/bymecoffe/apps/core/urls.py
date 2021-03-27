from django.urls import path

from . import views

urlpatterns = [
    path('login/', views.login, name = 'login'),
    path('logout/', auth_views.LogoutView.as_view(), name = 'logout'),
    path('social-auth', include('social_django.urls', namespace='social')),
]