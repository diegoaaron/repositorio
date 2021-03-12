
from django.urls import path, include

from rest_framework.routers import DefaultRouter

from .views import article_list, article_detail, ArticleAPIView, ArticleDetails, GenericAPIView, ArticleViewSet

router = DefaultRouter()
router.register('article', ArticleViewSet, basename='article')

urlpatterns = [
    path('viewset/', include(router.urls)),
    #path('article/', article_list, name = 'article'),
    path('article/', ArticleAPIView.as_view(), name = 'article1'),
    #path('detail/<int:pk>/', article_detail, name = 'detail'),
    path('detail/<int:id>/', ArticleDetails.as_view(), name = 'detail'),
    path('generic/article/<int:id>/', GenericAPIView.as_view(), name = 'detail2'),
]
