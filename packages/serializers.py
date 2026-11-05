from rest_framework import serializers
from .models import Package, PackageDay, PackagePricing


class PackageDaySerializer(serializers.ModelSerializer):
    class Meta:
        model = PackageDay
        fields = ['day', 'city', 'title', 'activities', 'stay', 'meals']


class PackagePricingSerializer(serializers.ModelSerializer):
    class Meta:
        model = PackagePricing
        fields = ['group', 'rate', 'vehicle']


class PackageListSerializer(serializers.ModelSerializer):
    """Lightweight — used for listing page and homepage cards."""
    class Meta:
        model = Package
        fields = [
            'id', 'title', 'subtitle', 'duration', 'cities',
            'starting_price', 'hero_img', 'img_alt',
            'features', 'pkg_label',
            'is_popular', 'min_duration_days', 'min_group', 'tags',
        ]


class PackageDetailSerializer(serializers.ModelSerializer):
    """Full detail — used for individual package pages."""
    days = PackageDaySerializer(many=True, read_only=True)
    pricing = PackagePricingSerializer(many=True, read_only=True)

    class Meta:
        model = Package
        fields = [
            'id', 'title', 'subtitle', 'duration', 'cities',
            'starting_price', 'hero_img', 'img_alt',
            'features', 'pkg_label',
            'places', 'activities', 'inclusions', 'exclusions',
            'is_popular', 'min_duration_days', 'min_group', 'tags',
            'meta_description',
            'days', 'pricing',
        ]
