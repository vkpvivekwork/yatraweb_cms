from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveUpdateAPIView
from rest_framework.permissions import AllowAny, IsAdminUser
from rest_framework.response import Response
from rest_framework import status
from .models import Booking
from .serializers import BookingSerializer, BookingAdminSerializer


# Maps query param → ORM lookup
# Each entry: 'param_name': ('orm_lookup', transform_fn or None)
BOOKING_FILTERS = {
    'status':           ('status',                  None),
    'page':             ('page_source',             None),
    'service':          ('services__contains',      None),
    'group':            ('group_type',              None),
    'itinerary_sent':   ('itinerary_sent',          lambda v: v.lower() == 'true'),
    'from':             ('created_at__date__gte',   None),
    'to':               ('created_at__date__lte',   None),
    'search':           ('name__icontains',         None),
}


class BookingCreateView(CreateAPIView):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    permission_classes = [AllowAny]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response(
            {
                'message': 'Enquiry received. We will contact you shortly.',
                'id': serializer.data['id'],
            },
            status=status.HTTP_201_CREATED,
        )


class BookingAdminListView(ListAPIView):
    serializer_class = BookingAdminSerializer
    permission_classes = [IsAdminUser]

    def get_queryset(self):
        qs = Booking.objects.all()
        params = self.request.query_params

        for param, (lookup, transform) in BOOKING_FILTERS.items():
            value = params.get(param)
            if value is not None:
                qs = qs.filter(**{lookup: transform(value) if transform else value})

        return qs


class BookingAdminDetailView(RetrieveUpdateAPIView):
    queryset = Booking.objects.all()
    serializer_class = BookingAdminSerializer
    permission_classes = [IsAdminUser]
    http_method_names = ['get', 'patch']
