from rest_framework import mixins, viewsets, permissions
from .models import Article
from .serializers import ArticleSerializer
from .pagination import StandardResultsSetPagination

class ArticleViewSet(viewsets.ModelViewSet):
    queryset = Article.objects.all().select_related('author').prefetch_related('language', 'tags').order_by('-publish_time')
    serializer_class = ArticleSerializer
    pagination_class = StandardResultsSetPagination
    http_method_names = ['get',]
    lookup_field = 'pk'