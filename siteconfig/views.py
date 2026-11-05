from rest_framework.views import APIView
from rest_framework.permissions import AllowAny, IsAdminUser
from rest_framework.response import Response
from rest_framework import status
from .models import SiteConfig
from .serializers import SiteConfigSerializer


class SiteConfigView(APIView):
    """
    GET  — returns the single site config row.
    PATCH — updates any fields on the config row.
    """

    def get_permissions(self):
        if self.request.method == 'PATCH':
            return [IsAdminUser()]
        return [AllowAny()]

    def get(self, request):
        config, _ = SiteConfig.objects.get_or_create(pk=1)
        serializer = SiteConfigSerializer(config)
        return Response(serializer.data)

    def patch(self, request):
        config, _ = SiteConfig.objects.get_or_create(pk=1)
        serializer = SiteConfigSerializer(config, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
