from rest_framework.generics import ListAPIView, RetrieveAPIView
from .models import Festival
from .serializers import FestivalListSerializer, FestivalDetailSerializer


FESTIVAL_FILTERS = {
    'city':     ('city__icontains',       None),
    'type':     ('festival_type',         None),
    'month':    ('month_of_occurrence__icontains', None),
    'deity':    ('deity__icontains',      None),
    'crowd':    ('crowd_level',           None),
    'featured': ('is_featured',           lambda v: True),
    'ghat':     ('related_ghats__slug',   None),
    'package':  ('related_packages__id',  None),
    'tag':      ('tags__contains',        None),
}


class FestivalListView(ListAPIView):
    serializer_class = FestivalListSerializer

    def get_queryset(self):
        qs = Festival.objects.filter(is_active=True)
        params = self.request.query_params

        for param, (lookup, transform) in FESTIVAL_FILTERS.items():
            value = params.get(param)
            if value is not None:
                qs = qs.filter(**{lookup: transform(value) if transform else value})

        return qs


class FestivalDetailView(RetrieveAPIView):
    queryset = Festival.objects.filter(is_active=True)
    serializer_class = FestivalDetailSerializer
    lookup_field = 'slug'
