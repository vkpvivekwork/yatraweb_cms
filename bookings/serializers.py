from rest_framework import serializers
from .models import Booking


class BookingSerializer(serializers.ModelSerializer):
    """Public serializer — used for POST from frontend forms."""

    class Meta:
        model = Booking
        fields = [
            'id',
            # contact
            'name', 'phone',
            # yatra plan
            'services', 'cities', 'start_date', 'num_days', 'num_people',
            # package
            'package_name', 'package_tier',
            # extras
            'form_data',
            # traveller context
            'group_type', 'arriving_from', 'customer_notes', 'customer_budget',
            # attribution (frontend sets these, not the user)
            'source', 'referrer_name', 'utm_campaign', 'page_source',
            # meta
            'created_at',
        ]
        read_only_fields = ['id', 'created_at']


class BookingAdminSerializer(serializers.ModelSerializer):
    """Admin serializer — full read + status/notes/itinerary update."""

    class Meta:
        model = Booking
        fields = [
            'id',
            # contact
            'name', 'phone',
            # yatra plan
            'services', 'cities', 'start_date', 'num_days', 'num_people',
            # package
            'package_name', 'package_tier',
            # extras
            'form_data',
            # traveller context
            'group_type', 'arriving_from', 'customer_notes', 'customer_budget',
            # attribution
            'source', 'referrer_name', 'utm_campaign', 'page_source',
            # itinerary
            'itinerary_sent', 'itinerary_sent_at',
            # admin/crm
            'status', 'internal_notes',
            # meta
            'created_at',
        ]
        read_only_fields = [
            'id', 'name', 'phone',
            'services', 'cities', 'start_date', 'num_days', 'num_people',
            'package_name', 'package_tier', 'form_data',
            'group_type', 'arriving_from', 'customer_notes', 'customer_budget',
            'source', 'referrer_name', 'utm_campaign', 'page_source',
            'created_at',
        ]
