from rest_framework.generics import ListAPIView, RetrieveAPIView
from .models import Package
from .serializers import PackageListSerializer, PackageDetailSerializer


# Maps query param → ORM lookup
# Each entry: 'param_name': ('orm_lookup', transform_fn or None)
PACKAGE_FILTERS = {
    'popular':  ('is_popular',          lambda v: True),
    'tags':     ('tags__contains',      None),
    'city':     ('cities__contains',    None),
    'duration': ('duration__icontains', None),
    'search':   ('title__icontains',    None),
    'min_days': ('min_duration_days__gte', int),
    'group':    ('min_group__icontains', None),
}


class PackageListView(ListAPIView):
    serializer_class = PackageListSerializer

    def get_queryset(self):
        qs = Package.objects.filter(is_active=True)
        params = self.request.query_params

        for param, (lookup, transform) in PACKAGE_FILTERS.items():
            value = params.get(param)
            if value is not None:
                qs = qs.filter(**{lookup: transform(value) if transform else value})

        return qs


class PackageDetailView(RetrieveAPIView):
    queryset = Package.objects.filter(is_active=True)
    serializer_class = PackageDetailSerializer
    lookup_field = 'id'
