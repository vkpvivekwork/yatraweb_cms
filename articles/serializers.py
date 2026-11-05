from rest_framework import serializers
from .models import ArticleCategory, Article


class ArticleCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ArticleCategory
        fields = ['id', 'name', 'slug', 'description', 'image_url', 'sort_order']


class ArticleListSerializer(serializers.ModelSerializer):
    """Lightweight — used for listing cards."""
    category = ArticleCategorySerializer(read_only=True)

    class Meta:
        model = Article
        fields = [
            'id', 'title', 'slug',
            'excerpt', 'featured_image', 'featured_image_alt',
            'category', 'content_type', 'article_type',
            'season', 'destinations',
            'primary_keyword',
            'status', 'published_at', 'is_featured', 'sort_order',
        ]


class ArticleDetailSerializer(serializers.ModelSerializer):
    """Full detail — includes body, SEO, related packages."""
    category         = ArticleCategorySerializer(read_only=True)
    related_packages = serializers.SlugRelatedField(many=True, read_only=True, slug_field='id')

    class Meta:
        model = Article
        fields = [
            'id', 'title', 'slug',
            'excerpt', 'body', 'featured_image', 'featured_image_alt',
            'category', 'content_type', 'article_type',
            'destinations', 'season', 'related_packages',
            'meta_title', 'meta_description', 'og_image_url',
            'canonical_url', 'primary_keyword', 'secondary_keywords',
            'status', 'published_at', 'is_featured', 'sort_order',
            'created_at', 'updated_at',
        ]
