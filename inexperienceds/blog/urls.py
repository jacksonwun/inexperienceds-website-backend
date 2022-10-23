from django.urls import path, include
from rest_framework import routers, serializers, viewsets

from .viewsets import ArticleViewSet

router = routers.DefaultRouter()
router.register(r'blog', ArticleViewSet, 'articles')

urlpatterns = [
    path('', include(router.urls)),
    ]