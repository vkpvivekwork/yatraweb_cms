from rest_framework import serializers
from .models import Festival


class FestivalListSerializer(serializers.ModelSerializer):
    """Lightweight — used for listing cards and homepage."""

    class Meta:
        model = Festival
        fields = [
            'id', 'name', 'name_hi', 'slug', 'tagline',
            'month_of_occurrence', 'typical_date',
            'image_url', 'image_alt',
            'festival_type', 'deity', 'city', 'tags',
            'crowd_level', 'advance_booking',
            'is_featured', 'sort_order',
        ]


class FestivalDetailSerializer(serializers.ModelSerializer):
    """Full detail — used for individual festival pages (programmatic SEO)."""
    primary_ghat     = serializers.SlugRelatedField(read_only=True, slug_field='slug')
    related_ghats    = serializers.SlugRelatedField(many=True, read_only=True, slug_field='slug')
    related_packages = serializers.SlugRelatedField(many=True, read_only=True, slug_field='id')
    related_articles = serializers.SlugRelatedField(many=True, read_only=True, slug_field='slug')

    class Meta:
        model = Festival
        fields = [
            'id', 'name', 'name_hi', 'slug', 'tagline',
            # timing
            'month_of_occurrence', 'typical_date', 'lunar_calendar',
            # content
            'description', 'significance', 'history',
            'what_happens', 'what_to_expect',
            'how_to_participate', 'best_viewpoint',
            # media
            'image_url', 'image_alt',
            # classification
            'festival_type', 'deity', 'city', 'tags',
            # practical
            'crowd_level', 'advance_booking', 'booking_tips', 'dress_code',
            # location
            'primary_ghat', 'related_ghats',
            # seo
            'meta_title', 'meta_description', 'og_image_url',
            'primary_keyword', 'secondary_keywords',
            # relations
            'related_packages', 'related_articles',
            # control
            'is_active', 'is_featured', 'sort_order',
            'created_at', 'updated_at',
        ]
