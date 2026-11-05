from django.urls import path
from .views import GhatListView, GhatDetailView

urlpatterns = [
    path('',              GhatListView.as_view(),   name='ghat-list'),
    path('<slug:slug>/',  GhatDetailView.as_view(), name='ghat-detail'),
]
