from django.contrib import admin
from .models import TravelStory, TravelStoryPhoto


class TravelStoryPhotoInline(admin.TabularInline):
    model = TravelStoryPhoto
    extra = 1
    fields = ['image_url', 'caption', 'order']


@admin.register(TravelStory)
class TravelStoryAdmin(admin.ModelAdmin):
    inlines = [TravelStoryPhotoInline]

    list_display = [
        'name', 'hometown', 'travel_type', 'package',
        'num_people', 'start_date', 'end_date',
        'rating', 'is_featured', 'is_approved', 'order',
    ]
    list_filter = ['is_featured', 'is_approved', 'travel_type', 'booking_source']
    search_fields = ['name', 'hometown', 'mobile', 'testimonial', 'highlight_quote']
    list_editable = ['is_featured', 'is_approved', 'order']
    readonly_fields = ['created_at']

    fieldsets = (
        ('Guest Info', {
            'fields': ('name', 'hometown', 'mobile', 'travel_type'),
        }),
        ('Trip Details', {
            'fields': ('package', 'places_visited', 'services_used', 'num_people', 'start_date', 'end_date'),
        }),
        ('Their Story', {
            'fields': ('highlight_quote', 'testimonial', 'rating'),
        }),
        ('Media', {
            'fields': ('featured_image', 'testimonial_video_url', 'testimonial_thumbnail', 'social_post_url', 'google_review_link'),
        }),
        ('Internal / Marketing', {
            'fields': ('booking_source',),
            'classes': ('collapse',),
        }),
        ('Control', {
            'fields': ('is_featured', 'is_approved', 'order', 'created_at'),
        }),
    )


@admin.register(TravelStoryPhoto)
class TravelStoryPhotoAdmin(admin.ModelAdmin):
    list_display = ['story', 'caption', 'order']
    list_filter = ['story']
    search_fields = ['story__name', 'caption']
