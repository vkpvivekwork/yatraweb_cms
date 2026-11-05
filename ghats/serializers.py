from rest_framework import serializers
from .models import Ghat


class GhatListSerializer(serializers.ModelSerializer):
    """Lightweight — used for listing cards and homepage."""

    class Meta:
        model = Ghat
        fields = [
            'id', 'name', 'name_hi', 'slug', 'nickname', 'tagline',
            'city', 'river', 'river_zone',
            'image_url', 'image_alt',
            'ghat_type', 'season', 'tags',
            'aarti_time', 'boat_available', 'photography_allowed',
            'is_featured', 'sort_order',
        ]


class GhatDetailSerializer(serializers.ModelSerializer):
    """Full detail — used for individual ghat pages (programmatic SEO)."""
    related_packages = serializers.SlugRelatedField(many=True, read_only=True, slug_field='id')
    related_articles = serializers.SlugRelatedField(many=True, read_only=True, slug_field='slug')

    class Meta:
        model = Ghat
        fields = [
            'id', 'name', 'name_hi', 'slug', 'nickname', 'tagline',
            # location
            'city', 'river', 'river_zone', 'distance_from_station', 'coordinates',
            # content
            'description', 'significance', 'history',
            'best_time', 'what_to_expect', 'how_to_reach', 'dress_code',
            # media
            'image_url', 'image_alt',
            # classification
            'ghat_type', 'season', 'tags',
            # facts
            'activities', 'important_places', 'nearby_temples',
            'festivals_celebrated', 'aarti_time',
            'built_by', 'built_in',
            'photography_allowed', 'boat_available',
            # seo
            'meta_title', 'meta_description', 'og_image_url',
            'primary_keyword', 'secondary_keywords',
            # relations
            'related_packages', 'related_articles',
            # control
            'is_active', 'is_featured', 'sort_order',
            'created_at', 'updated_at',
        ]
