from django.contrib import admin
from .models import Ghat


@admin.register(Ghat)
class GhatAdmin(admin.ModelAdmin):
    list_display  = ['name', 'name_hi', 'city', 'river', 'ghat_type', 'boat_available', 'is_featured', 'is_active', 'sort_order']
    list_editable = ['is_active', 'is_featured', 'sort_order']
    list_filter   = ['is_active', 'is_featured', 'ghat_type', 'river_zone', 'season', 'boat_available', 'city']
    search_fields = ['name', 'city', 'river', 'primary_keyword']
    prepopulated_fields = {'slug': ('name',)}
    filter_horizontal = ['related_packages', 'related_articles']
    fieldsets = (
        ('Identity', {
            'fields': ('name', 'name_hi', 'slug', 'nickname', 'tagline')
        }),
        ('Location', {
            'fields': ('city', 'river', 'river_zone', 'distance_from_station', 'coordinates')
        }),
        ('Content', {
            'fields': ('description', 'significance', 'history', 'best_time', 'what_to_expect', 'how_to_reach', 'dress_code')
        }),
        ('Media', {
            'fields': ('image_url', 'image_alt')
        }),
        ('Classification', {
            'fields': ('ghat_type', 'season', 'tags')
        }),
        ('Facts & Activities', {
            'fields': ('activities', 'important_places', 'nearby_temples', 'festivals_celebrated', 'aarti_time', 'built_by', 'built_in', 'photography_allowed', 'boat_available')
        }),
        ('SEO', {
            'fields': ('meta_title', 'meta_description', 'og_image_url', 'primary_keyword', 'secondary_keywords')
        }),
        ('Relations', {
            'fields': ('related_packages', 'related_articles')
        }),
        ('Control', {
            'fields': ('is_active', 'is_featured', 'sort_order')
        }),
    )
