from django.contrib import admin
from .models import Package, PackageDay, PackagePricing


class PackageDayInline(admin.TabularInline):
    model = PackageDay
    extra = 1
    fields = ['order', 'day', 'city', 'title', 'activities', 'stay', 'meals']


class PackagePricingInline(admin.TabularInline):
    model = PackagePricing
    extra = 1
    fields = ['order', 'group', 'rate', 'vehicle']


@admin.register(Package)
class PackageAdmin(admin.ModelAdmin):
    list_display = ['title', 'duration', 'starting_price', 'is_popular', 'is_active', 'order']
    list_editable = ['is_active', 'is_popular', 'order']
    list_filter = ['is_active', 'is_popular']
    search_fields = ['title', 'subtitle']
    prepopulated_fields = {'id': ('title',)}
    inlines = [PackageDayInline, PackagePricingInline]
    fieldsets = (
        ('Basic Info', {
            'fields': ('id', 'title', 'subtitle', 'duration', 'cities', 'starting_price', 'min_duration_days', 'min_group')
        }),
        ('Media', {
            'fields': ('hero_img', 'img_alt')
        }),
        ('Homepage Card', {
            'fields': ('features', 'pkg_label')
        }),
        ('Detail Page', {
            'fields': ('places', 'activities', 'inclusions', 'exclusions')
        }),
        ('Settings', {
            'fields': ('is_popular', 'is_active', 'order', 'tags', 'meta_description')
        }),
    )
