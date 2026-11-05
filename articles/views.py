from rest_framework.generics import ListAPIView, RetrieveAPIView
from .models import ArticleCategory, Article
from .serializers import ArticleCategorySerializer, ArticleListSerializer, ArticleDetailSerializer


class ArticleCategoryListView(ListAPIView):
    queryset = ArticleCategory.objects.all()
    serializer_class = ArticleCategorySerializer


class ArticleListView(ListAPIView):
    serializer_class = ArticleListSerializer

    def get_queryset(self):
        qs = Article.objects.filter(status='published')

        article_type  = self.request.query_params.get('type')
        content_type  = self.request.query_params.get('content')
        category      = self.request.query_params.get('category')
        season        = self.request.query_params.get('season')
        package       = self.request.query_params.get('package')
        featured      = self.request.query_params.get('featured')
        keyword       = self.request.query_params.get('keyword')

        if article_type:
            qs = qs.filter(article_type=article_type)
        if content_type:
            qs = qs.filter(content_type=content_type)
        if category:
            qs = qs.filter(category__slug=category)
        if season:
            qs = qs.filter(season__in=[season, 'any'])
        if package:
            qs = qs.filter(related_packages__id=package)
        if featured:
            qs = qs.filter(is_featured=True)
        if keyword:
            qs = qs.filter(primary_keyword__icontains=keyword)

        return qs


class ArticleDetailView(RetrieveAPIView):
    queryset = Article.objects.filter(status='published')
    serializer_class = ArticleDetailSerializer
    lookup_field = 'slug'


class ArticleFeaturedView(ListAPIView):
    serializer_class = ArticleListSerializer
    queryset = Article.objects.filter(status='published', is_featured=True)
