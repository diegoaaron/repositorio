from django.urls import include, path, patterns

from rest_framework.urlpatterns import format_suffix_patterns

from . import views


urlpatterns = patterns('api.views',
    #path('surveys/', views.survey_list, name='survey_list'),
    #path('surveys/<pk>/', views.survey_details, name='survey_detail'),
    path('surveys/', views.SurveyList.as_view(), name='survey_list'),
    path('surveys/<pk>/', views.SurveyDetails.as_view(), name='survey_detail'),
)
urlpatterns = format_suffix_patterns(urlpatterns)