from django.contrib import admin
from .models import Booking


@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display  = ['name', 'phone', 'city_list', 'service_list', 'group_type', 'status', 'created_at']
    list_filter   = ['status', 'group_type', 'package_tier', 'source']
    search_fields = ['name', 'phone', 'package_name', 'arriving_from', 'referrer_name', 'utm_campaign']
    list_editable = ['status']
    date_hierarchy = 'created_at'

    readonly_fields = [
        'name', 'phone',
        'services', 'cities', 'start_date', 'num_days', 'num_people',
        'package_name', 'package_tier',
        'form_data',
        'group_type', 'arriving_from', 'customer_notes', 'customer_budget',
        'source', 'referrer_name', 'utm_campaign', 'page_source',
        'created_at',
    ]

    fieldsets = (
        ('Contact', {
            'fields': ('name', 'phone'),
        }),
        ('Yatra Plan', {
            'fields': ('services', 'cities', 'start_date', 'num_days', 'num_people'),
        }),
        ('Package', {
            'fields': ('package_name', 'package_tier'),
        }),
        ('Service Extras', {
            'fields': ('form_data',),
        }),
        ('Traveller Context', {
            'fields': ('group_type', 'arriving_from', 'customer_notes', 'customer_budget'),
        }),
        ('Attribution', {
            'classes': ('collapse',),
            'fields': ('source', 'referrer_name', 'utm_campaign', 'page_source'),
        }),
        ('Admin / CRM', {
            'fields': ('status', 'internal_notes', 'created_at'),
        }),
    )

    def city_list(self, obj):
        return ', '.join(obj.cities) if obj.cities else '—'
    city_list.short_description = 'Cities'

    def service_list(self, obj):
        return ', '.join(obj.services) if obj.services else '—'
    service_list.short_description = 'Services'
