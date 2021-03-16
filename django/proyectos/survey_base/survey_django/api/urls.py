from django.urls import include, path

from . import views

urlpatterns = [
    path('surveys/', views.survey_list, name='survey_list'),
    path('surveys/<pk>/', views.survey_details, name='survey_list'),
]