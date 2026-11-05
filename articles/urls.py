from django.urls import path
from .views import (
    ArticleCategoryListView,
    ArticleListView,
    ArticleDetailView,
    ArticleFeaturedView,
)

urlpatterns = [
    path('',                ArticleListView.as_view(),         name='article-list'),
    path('featured/',       ArticleFeaturedView.as_view(),     name='article-featured'),
    path('categories/',     ArticleCategoryListView.as_view(), name='article-category-list'),
    path('<slug:slug>/',    ArticleDetailView.as_view(),       name='article-detail'),
]
