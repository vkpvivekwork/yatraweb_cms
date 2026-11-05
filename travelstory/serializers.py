from rest_framework import serializers
from .models import TravelStory, TravelStoryPhoto


class TravelStoryPhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = TravelStoryPhoto
        fields = ['id', 'image_url', 'caption', 'order']


class TravelStoryListSerializer(serializers.ModelSerializer):
    """Lightweight — used for homepage testimonial slider and listing page."""
    num_days = serializers.ReadOnlyField()

    class Meta:
        model = TravelStory
        fields = [
            'id',
            'name', 'hometown', 'travel_type',
            'package',
            'num_people', 'num_days', 'start_date', 'end_date',
            'highlight_quote', 'rating',
            'featured_image',
            'testimonial_video_url', 'testimonial_thumbnail',
            'social_post_url', 'google_review_link',
            'is_featured',
        ]


class TravelStoryDetailSerializer(serializers.ModelSerializer):
    """Full detail — includes photos and all story fields."""
    photos = TravelStoryPhotoSerializer(many=True, read_only=True)
    num_days = serializers.ReadOnlyField()

    class Meta:
        model = TravelStory
        fields = [
            'id',
            'name', 'hometown', 'travel_type',
            'package',
            'places_visited', 'services_used',
            'num_people', 'num_days', 'start_date', 'end_date',
            'highlight_quote', 'testimonial', 'rating',
            'featured_image',
            'testimonial_video_url', 'testimonial_thumbnail',
            'social_post_url', 'google_review_link',
            'is_featured',
            'photos',
        ]
        # mobile and booking_source are internal — excluded from all public serializers
