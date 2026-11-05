from django.db import models


class Ghat(models.Model):

    GHAT_TYPE_CHOICES = [
        ('bathing',       'Bathing'),
        ('cremation',     'Cremation'),
        ('aarti',         'Aarti'),
        ('religious',     'Religious'),
        ('recreational',  'Recreational'),
    ]

    RIVER_ZONE_CHOICES = [
        ('northern', 'Northern'),
        ('central',  'Central'),
        ('southern', 'Southern'),
    ]

    SEASON_CHOICES = [
        ('any',      'Any'),
        ('winter',   'Winter'),
        ('summer',   'Summer'),
        ('monsoon',  'Monsoon'),
        ('festive',  'Festive'),
    ]

    # ── Identity ──────────────────────────────────────────────────────────────
    name     = models.CharField(max_length=200)
    name_hi  = models.CharField(max_length=200, blank=True)
    slug     = models.SlugField(unique=True, max_length=250)
    nickname = models.CharField(max_length=200, blank=True)
    tagline  = models.CharField(max_length=300, blank=True)

    # ── Location ──────────────────────────────────────────────────────────────
    city                   = models.CharField(max_length=100)
    river                  = models.CharField(max_length=100)
    river_zone             = models.CharField(max_length=20, choices=RIVER_ZONE_CHOICES, blank=True)
    distance_from_station  = models.CharField(max_length=200, blank=True)
    coordinates            = models.CharField(max_length=50, blank=True,
                                              help_text='lat,lng — e.g. 25.2677,82.9913')

    # ── Content ───────────────────────────────────────────────────────────────
    description    = models.TextField()
    significance   = models.TextField(blank=True)
    history        = models.TextField(blank=True)
    best_time      = models.CharField(max_length=300, blank=True)
    what_to_expect = models.TextField(blank=True)
    how_to_reach   = models.TextField(blank=True)
    dress_code     = models.CharField(max_length=300, blank=True)

    # ── Media ─────────────────────────────────────────────────────────────────
    image_url  = models.CharField(max_length=500)
    image_alt  = models.CharField(max_length=300, blank=True)

    # ── Classification ────────────────────────────────────────────────────────
    ghat_type = models.CharField(max_length=20, choices=GHAT_TYPE_CHOICES, default='bathing')
    season    = models.CharField(max_length=20, choices=SEASON_CHOICES, default='any', blank=True)
    tags      = models.JSONField(default=list, blank=True)

    # ── Facts & Activities ────────────────────────────────────────────────────
    activities          = models.JSONField(default=list, blank=True)
    important_places    = models.JSONField(default=list, blank=True)
    nearby_temples      = models.JSONField(default=list, blank=True)
    festivals_celebrated = models.JSONField(default=list, blank=True)
    aarti_time          = models.CharField(max_length=100, blank=True)
    built_by            = models.CharField(max_length=200, blank=True)
    built_in            = models.CharField(max_length=100, blank=True)
    photography_allowed = models.BooleanField(default=True)
    boat_available      = models.BooleanField(default=False)

    # ── SEO ───────────────────────────────────────────────────────────────────
    meta_title         = models.CharField(max_length=200, blank=True)
    meta_description   = models.TextField(blank=True)
    og_image_url       = models.CharField(max_length=500, blank=True)
    primary_keyword    = models.CharField(max_length=200, blank=True)
    secondary_keywords = models.JSONField(default=list, blank=True)

    # ── Relations ─────────────────────────────────────────────────────────────
    related_packages = models.ManyToManyField(
        'packages.Package',
        blank=True,
        related_name='ghats',
    )
    related_articles = models.ManyToManyField(
        'articles.Article',
        blank=True,
        related_name='ghats',
    )

    # ── Control ───────────────────────────────────────────────────────────────
    is_active  = models.BooleanField(default=True)
    is_featured = models.BooleanField(default=False)
    sort_order = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['sort_order', 'name']
        verbose_name = 'Ghat'
        verbose_name_plural = 'Ghats'

    def __str__(self):
        return f'{self.name} — {self.city}'
