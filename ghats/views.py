from rest_framework.generics import ListAPIView, RetrieveAPIView
from .models import Ghat
from .serializers import GhatListSerializer, GhatDetailSerializer


GHAT_FILTERS = {
    'city':       ('city__icontains',    None),
    'river':      ('river__icontains',   None),
    'type':       ('ghat_type',          None),
    'zone':       ('river_zone',         None),
    'season':     ('season__in',         lambda v: [v, 'any']),
    'featured':   ('is_featured',        lambda v: True),
    'boat':       ('boat_available',     lambda v: v.lower() == 'true'),
    'package':    ('related_packages__id', None),
    'tag':        ('tags__contains',     None),
}


class GhatListView(ListAPIView):
    serializer_class = GhatListSerializer

    def get_queryset(self):
        qs = Ghat.objects.filter(is_active=True)
        params = self.request.query_params

        for param, (lookup, transform) in GHAT_FILTERS.items():
            value = params.get(param)
            if value is not None:
                qs = qs.filter(**{lookup: transform(value) if transform else value})

        return qs


class GhatDetailView(RetrieveAPIView):
    queryset = Ghat.objects.filter(is_active=True)
    serializer_class = GhatDetailSerializer
    lookup_field = 'slug'
