from django.contrib import admin
from .models import ArticleCategory, Article


@admin.register(ArticleCategory)
class ArticleCategoryAdmin(admin.ModelAdmin):
    list_display  = ['name', 'slug', 'sort_order']
    list_editable = ['sort_order']
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display  = ['title', 'article_type', 'content_type', 'category', 'status', 'is_featured', 'published_at', 'sort_order']
    list_editable = ['status', 'is_featured', 'sort_order']
    list_filter   = ['status', 'article_type', 'content_type', 'category', 'season', 'is_featured']
    search_fields = ['title', 'excerpt', 'primary_keyword']
    prepopulated_fields = {'slug': ('title',)}
    filter_horizontal = ['related_packages']
    fieldsets = (
        ('Identity', {
            'fields': ('title', 'slug')
        }),
        ('Content', {
            'fields': ('excerpt', 'body', 'featured_image', 'featured_image_alt')
        }),
        ('Classification', {
            'fields': ('category', 'content_type', 'article_type')
        }),
        ('Travel Context', {
            'fields': ('destinations', 'season', 'related_packages')
        }),
        ('SEO', {
            'fields': ('meta_title', 'meta_description', 'og_image_url', 'canonical_url', 'primary_keyword', 'secondary_keywords')
        }),
        ('Publishing', {
            'fields': ('status', 'published_at', 'is_featured', 'sort_order')
        }),
    )
