from rest_framework.generics import ListAPIView, RetrieveAPIView
from .models import GalleryPhoto
from .serializers import GalleryPhotoListSerializer, GalleryPhotoDetailSerializer


class GalleryPhotoListView(ListAPIView):
    serializer_class = GalleryPhotoListSerializer

    def get_queryset(self):
        qs = GalleryPhoto.objects.filter(is_active=True)

        package  = self.request.query_params.get('package')
        section  = self.request.query_params.get('section')
        category = self.request.query_params.get('category')
        season   = self.request.query_params.get('season')
        featured = self.request.query_params.get('featured')

        if package:
            qs = qs.filter(linked_packages__id=package)
        if section:
            qs = qs.filter(section__in=[section, 'all'])
        if category:
            qs = qs.filter(category=category)
        if season:
            qs = qs.filter(season__in=[season, 'any'])
        if featured:
            qs = qs.filter(is_featured=True)

        return qs


class GalleryPhotoDetailView(RetrieveAPIView):
    queryset = GalleryPhoto.objects.filter(is_active=True)
    serializer_class = GalleryPhotoDetailSerializer
