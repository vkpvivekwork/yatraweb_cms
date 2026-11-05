from django.contrib import admin
from .models import GalleryPhoto


@admin.register(GalleryPhoto)
class GalleryPhotoAdmin(admin.ModelAdmin):
    list_display  = ['__str__', 'category', 'section', 'file_type', 'source', 'is_featured', 'is_active', 'sort_order']
    list_editable = ['is_active', 'is_featured', 'sort_order']
    list_filter   = ['is_active', 'is_featured', 'category', 'section', 'file_type', 'source', 'season']
    search_fields = ['title', 'caption', 'location', 'photographer']
    filter_horizontal = ['linked_packages']
    fieldsets = (
        ('Identity', {
            'fields': ('title',)
        }),
        ('Media', {
            'fields': ('image_url', 'thumbnail_url', 'file_type', 'video_url', 'width', 'height')
        }),
        ('Content', {
            'fields': ('alt_text', 'caption', 'description')
        }),
        ('Classification', {
            'fields': ('category', 'tags', 'location', 'season', 'section')
        }),
        ('Source', {
            'fields': ('source', 'photographer', 'source_url', 'taken_on')
        }),
        ('Relations', {
            'fields': ('linked_packages',)
        }),
        ('Control', {
            'fields': ('is_active', 'is_featured', 'sort_order')
        }),
    )
