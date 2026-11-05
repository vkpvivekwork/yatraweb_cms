from django.urls import path
from .views import TravelStoryListView, TravelStoryFeaturedView, TravelStoryDetailView

urlpatterns = [
    path('', TravelStoryListView.as_view(), name='travelstory-list'),
    path('featured/', TravelStoryFeaturedView.as_view(), name='travelstory-featured'),
    path('<int:pk>/', TravelStoryDetailView.as_view(), name='travelstory-detail'),
]
