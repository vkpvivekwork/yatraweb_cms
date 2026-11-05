from django.urls import path
from .views import FestivalListView, FestivalDetailView

urlpatterns = [
    path('',             FestivalListView.as_view(),   name='festival-list'),
    path('<slug:slug>/', FestivalDetailView.as_view(), name='festival-detail'),
]
