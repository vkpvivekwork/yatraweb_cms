from django.db import models


def _default_aarti_times():
    return [
        "6:00 PM", "6:15 PM", "6:30 PM", "6:45 PM",
        "7:00 PM", "7:15 PM", "7:15 PM", "7:00 PM",
        "6:30 PM", "6:15 PM", "5:45 PM", "5:45 PM",
    ]


class SiteConfig(models.Model):

    # ── Identity ──────────────────────────────────────────────────────────────
    business_name = models.CharField(max_length=200, default='YatraKSathi')
    tagline       = models.CharField(max_length=300, default='आपके हर सफर का साथी — YatraKSathi')

    # ── Contact ───────────────────────────────────────────────────────────────
    whatsapp_number = models.CharField(max_length=20, default='919277472279',
                                       help_text='Digits only with country code, e.g. 919277472279')
    phone_alt       = models.CharField(max_length=20, blank=True)
    email           = models.EmailField(blank=True)
    address         = models.TextField(blank=True)

    # ── Social ────────────────────────────────────────────────────────────────
    instagram_url   = models.CharField(max_length=500, blank=True)
    facebook_url    = models.CharField(max_length=500, blank=True)
    youtube_url     = models.CharField(max_length=500, blank=True)
    google_maps_url = models.CharField(max_length=500, blank=True)

    # ── Reviews ───────────────────────────────────────────────────────────────
    google_review_url = models.CharField(max_length=500, blank=True)
    tripadvisor_url   = models.CharField(max_length=500, blank=True)

    # ── Operations ────────────────────────────────────────────────────────────
    aarti_times        = models.JSONField(
        default=_default_aarti_times,
        help_text='List of 12 monthly evening aarti times, e.g. ["6:00 PM", "6:15 PM", ...]'
    )
    booking_open       = models.BooleanField(default=True, help_text='Uncheck to pause all new bookings')
    booking_closed_msg = models.CharField(max_length=300, blank=True,
                                          help_text='Shown on booking form when booking_open is False')

    # ── SEO ───────────────────────────────────────────────────────────────────
    meta_title       = models.CharField(max_length=200, blank=True)
    meta_description = models.TextField(blank=True)
    og_image_url     = models.CharField(max_length=500, blank=True)

    # ── Analytics ─────────────────────────────────────────────────────────────
    google_analytics_id = models.CharField(max_length=50, blank=True,
                                           help_text='e.g. G-XXXXXXXXXX')

    class Meta:
        verbose_name = 'Site Configuration'
        verbose_name_plural = 'Site Configuration'

    def __str__(self):
        return self.business_name

    def save(self, *args, **kwargs):
        self.pk = 1  # singleton — always overwrite the same row
        super().save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        pass  # prevent deletion
