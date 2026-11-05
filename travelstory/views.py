from rest_framework.generics import ListAPIView, RetrieveAPIView
from .models import TravelStory
from .serializers import TravelStoryListSerializer, TravelStoryDetailSerializer


class TravelStoryListView(ListAPIView):
    """All approved stories — used for listing/gallery page."""
    serializer_class = TravelStoryListSerializer

    def get_queryset(self):
        return TravelStory.objects.filter(is_approved=True)


class TravelStoryFeaturedView(ListAPIView):
    """Featured approved stories only — used for homepage testimonial slider."""
    serializer_class = TravelStoryListSerializer

    def get_queryset(self):
        return TravelStory.objects.filter(is_approved=True, is_featured=True)


class TravelStoryDetailView(RetrieveAPIView):
    """Full story with photos — used for individual story page."""
    serializer_class = TravelStoryDetailSerializer

    def get_queryset(self):
        return TravelStory.objects.filter(is_approved=True)
