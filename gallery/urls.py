from django.urls import path
from .views import GalleryPhotoListView, GalleryPhotoDetailView

urlpatterns = [
    path('', GalleryPhotoListView.as_view(), name='gallery-list'),
    path('<int:pk>/', GalleryPhotoDetailView.as_view(), name='gallery-detail'),
]
