from rest_framework import serializers
from .models import SiteConfig


class SiteConfigSerializer(serializers.ModelSerializer):

    class Meta:
        model = SiteConfig
        fields = [
            # identity
            'business_name', 'tagline',
            # contact
            'whatsapp_number', 'phone_alt', 'email', 'address',
            # social
            'instagram_url', 'facebook_url', 'youtube_url', 'google_maps_url',
            # reviews
            'google_review_url', 'tripadvisor_url',
            # operations
            'aarti_times', 'booking_open', 'booking_closed_msg',
            # seo
            'meta_title', 'meta_description', 'og_image_url',
            # analytics
            'google_analytics_id',
        ]
