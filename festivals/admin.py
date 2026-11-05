from django.contrib import admin
from .models import Festival


@admin.register(Festival)
class FestivalAdmin(admin.ModelAdmin):
    list_display  = ['name', 'name_hi', 'city', 'festival_type', 'month_of_occurrence', 'crowd_level', 'is_featured', 'is_active', 'sort_order']
    list_editable = ['is_active', 'is_featured', 'sort_order']
    list_filter   = ['is_active', 'is_featured', 'festival_type', 'city', 'crowd_level', 'advance_booking']
    search_fields = ['name', 'city', 'deity', 'primary_keyword']
    prepopulated_fields = {'slug': ('name',)}
    filter_horizontal = ['related_ghats', 'related_packages', 'related_articles']
    fieldsets = (
        ('Identity', {
            'fields': ('name', 'name_hi', 'slug', 'tagline')
        }),
        ('Timing', {
            'fields': ('month_of_occurrence', 'typical_date', 'lunar_calendar')
        }),
        ('Content', {
            'fields': ('description', 'significance', 'history', 'what_happens', 'what_to_expect', 'how_to_participate', 'best_viewpoint')
        }),
        ('Media', {
            'fields': ('image_url', 'image_alt')
        }),
        ('Classification', {
            'fields': ('festival_type', 'deity', 'city', 'tags')
        }),
        ('Practical Info', {
            'fields': ('crowd_level', 'advance_booking', 'booking_tips', 'dress_code')
        }),
        ('Location', {
            'fields': ('primary_ghat', 'related_ghats')
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
