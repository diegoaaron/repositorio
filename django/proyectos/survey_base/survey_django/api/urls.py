from django.urls import include, path

from . import views

urlpatterns = [
    #path('surveys/', views.survey_list, name='survey_list'),
    #path('surveys/<pk>/', views.survey_details, name='survey_detail'),
    path('surveys/', views.SurveyList.as_view(), name='survey_list'),
    path('surveys/<pk>/', views.SurveyDetails.as_view(), name='survey_detail'),

]