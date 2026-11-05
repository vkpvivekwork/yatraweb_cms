from django.db import models


class Booking(models.Model):
    STATUS_CHOICES = [
        ('new', 'New'),
        ('contacted', 'Contacted'),
        ('confirmed', 'Confirmed'),
        ('cancelled', 'Cancelled'),
    ]

    TIER_CHOICES = [
        ('basic', 'Basic'),
        ('standard', 'Standard'),
        ('premium', 'Premium'),
        ('custom', 'Custom'),
    ]

    GROUP_TYPE_CHOICES = [
        ('solo', 'Solo'),
        ('couple', 'Couple'),
        ('family', 'Family'),
        ('group', 'Group'),
        ('corporate', 'Corporate'),
        ('pilgrimage', 'Pilgrimage'),
        ('honeymoon', 'Honeymoon'),
    ]

    # ── Contact ──────────────────────────────────────────────────────────────
    name  = models.CharField(max_length=200)
    phone = models.CharField(max_length=20)

    # ── Yatra Plan ───────────────────────────────────────────────────────────
    services   = models.JSONField(default=list, help_text='e.g. ["tour","cab"]')
    cities     = models.JSONField(default=list, help_text='e.g. ["kashi","ayodhya"]')
    start_date = models.DateField(null=True, blank=True)
    num_days   = models.CharField(max_length=10, blank=True, help_text='"2", "3", "6-7", "8+"')
    num_people = models.PositiveIntegerField(default=2)

    # ── Package ───────────────────────────────────────────────────────────────
    package_name = models.CharField(max_length=200, blank=True)
    package_tier = models.CharField(max_length=20, choices=TIER_CHOICES, blank=True)

    # ── Service-specific extras ───────────────────────────────────────────────
    form_data = models.JSONField(default=dict, blank=True,
                                 help_text='Car type, pickup, boat slot, hotel area, etc.')

    # ── Traveller context ─────────────────────────────────────────────────────
    group_type    = models.CharField(max_length=20, choices=GROUP_TYPE_CHOICES, blank=True)
    arriving_from = models.CharField(max_length=200, blank=True,
                                     help_text='e.g. Delhi, Mumbai, Varanasi Jn, Already in city')
    customer_notes  = models.TextField(blank=True,
                                       help_text='Elders/kids, special puja, food prefs, etc.')
    customer_budget = models.CharField(max_length=100, blank=True,
                                       help_text='e.g. Under ₹5,000 / ₹5k–15k / ₹15k–30k / ₹30k+')

    # ── Attribution (internal — not exposed publicly) ─────────────────────────
    source        = models.CharField(max_length=100, blank=True,
                                     help_text='Google / Instagram / WhatsApp / Referral / Walk-in / Facebook Ads')
    referrer_name = models.CharField(max_length=200, blank=True)
    utm_campaign  = models.CharField(max_length=200, blank=True)
    page_source   = models.CharField(max_length=100, blank=True,
                                     help_text='homepage / travel-itinerary / package-detail / contact')

    # ── Itinerary ─────────────────────────────────────────────────────────────
    itinerary_sent    = models.BooleanField(default=False,
                                            help_text='Was a travel itinerary sent to this customer?')
    itinerary_sent_at = models.DateTimeField(null=True, blank=True,
                                             help_text='When the itinerary was sent')


    # ── Admin / CRM ───────────────────────────────────────────────────────────
    status         = models.CharField(max_length=20, choices=STATUS_CHOICES, default='new')
    internal_notes = models.TextField(blank=True, help_text='Internal notes for the team')
    created_at     = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        cities = ', '.join(self.cities) if self.cities else '—'
        return f'{self.name} ({cities}) — {self.created_at.strftime("%d %b %Y")}'
