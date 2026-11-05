from rest_framework import serializers
from .models import GalleryPhoto


class GalleryPhotoListSerializer(serializers.ModelSerializer):
    """Lightweight — used for gallery grid, ribbon, footer strip."""

    class Meta:
        model = GalleryPhoto
        fields = [
            'id', 'title',
            'image_url', 'thumbnail_url', 'file_type', 'video_url',
            'alt_text', 'caption',
            'category', 'section', 'season',
            'is_featured', 'sort_order',
        ]


class GalleryPhotoDetailSerializer(serializers.ModelSerializer):
    """Full detail — includes all fields."""
    linked_packages = serializers.SlugRelatedField(
        many=True,
        read_only=True,
        slug_field='id',
    )

    class Meta:
        model = GalleryPhoto
        fields = [
            'id', 'title',
            'image_url', 'thumbnail_url', 'file_type', 'video_url',
            'width', 'height',
            'alt_text', 'caption', 'description',
            'category', 'tags', 'location', 'season', 'section',
            'source', 'photographer', 'source_url', 'taken_on',
            'linked_packages',
            'is_active', 'is_featured', 'sort_order',
            'created_at', 'updated_at',
        ]
