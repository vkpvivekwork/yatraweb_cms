from django.contrib import admin
from .models import SiteConfig


@admin.register(SiteConfig)
class SiteConfigAdmin(admin.ModelAdmin):
    fieldsets = (
        ('Identity', {
            'fields': ('business_name', 'tagline')
        }),
        ('Contact', {
            'fields': ('whatsapp_number', 'phone_alt', 'email', 'address')
        }),
        ('Social', {
            'fields': ('instagram_url', 'facebook_url', 'youtube_url', 'google_maps_url')
        }),
        ('Reviews', {
            'fields': ('google_review_url', 'tripadvisor_url')
        }),
        ('Operations', {
            'fields': ('aarti_times', 'booking_open', 'booking_closed_msg')
        }),
        ('SEO', {
            'fields': ('meta_title', 'meta_description', 'og_image_url')
        }),
        ('Analytics', {
            'fields': ('google_analytics_id',)
        }),
    )

    def has_add_permission(self, request):
        # only one row allowed — hide Add button if it already exists
        return not SiteConfig.objects.exists()

    def has_delete_permission(self, request, obj=None):
        return False
