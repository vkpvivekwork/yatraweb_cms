from django.db import models


class Festival(models.Model):

    FESTIVAL_TYPE_CHOICES = [
        ('religious',  'Religious'),
        ('cultural',   'Cultural'),
        ('seasonal',   'Seasonal'),
        ('national',   'National'),
    ]

    CROWD_LEVEL_CHOICES = [
        ('low',     'Low'),
        ('medium',  'Medium'),
        ('high',    'High'),
        ('massive', 'Massive'),
    ]

    # ── Identity ──────────────────────────────────────────────────────────────
    name    = models.CharField(max_length=200)
    name_hi = models.CharField(max_length=200, blank=True)
    slug    = models.SlugField(unique=True, max_length=250)
    tagline = models.CharField(max_length=300, blank=True)

    # ── Timing ────────────────────────────────────────────────────────────────
    month_of_occurrence = models.CharField(max_length=100,
                                           help_text='e.g. October – November')
    typical_date        = models.CharField(max_length=200, blank=True,
                                           help_text='e.g. Kartik Purnima — full moon of Kartik month')
    lunar_calendar      = models.BooleanField(default=False,
                                              help_text='Is the date based on the Hindu lunar calendar?')

    # ── Content ───────────────────────────────────────────────────────────────
    description        = models.TextField()
    significance       = models.TextField(blank=True)
    history            = models.TextField(blank=True)
    what_happens       = models.TextField(blank=True)
    what_to_expect     = models.TextField(blank=True)
    how_to_participate = models.TextField(blank=True)
    best_viewpoint     = models.CharField(max_length=300, blank=True)

    # ── Media ─────────────────────────────────────────────────────────────────
    image_url  = models.CharField(max_length=500)
    image_alt  = models.CharField(max_length=300, blank=True)

    # ── Classification ────────────────────────────────────────────────────────
    festival_type = models.CharField(max_length=20, choices=FESTIVAL_TYPE_CHOICES, default='religious')
    deity         = models.CharField(max_length=200, blank=True)
    city          = models.CharField(max_length=100)
    tags          = models.JSONField(default=list, blank=True)

    # ── Practical Info ────────────────────────────────────────────────────────
    crowd_level      = models.CharField(max_length=20, choices=CROWD_LEVEL_CHOICES, blank=True)
    advance_booking  = models.BooleanField(default=False)
    booking_tips     = models.TextField(blank=True)
    dress_code       = models.CharField(max_length=300, blank=True)

    # ── Location Relations ────────────────────────────────────────────────────
    primary_ghat  = models.ForeignKey(
        'ghats.Ghat',
        null=True, blank=True,
        on_delete=models.SET_NULL,
        related_name='primary_festivals',
    )
    related_ghats = models.ManyToManyField(
        'ghats.Ghat',
        blank=True,
        related_name='festivals',
    )

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
        related_name='festivals',
    )
    related_articles = models.ManyToManyField(
        'articles.Article',
        blank=True,
        related_name='festivals',
    )

    # ── Control ───────────────────────────────────────────────────────────────
    is_active  = models.BooleanField(default=True)
    is_featured = models.BooleanField(default=False)
    sort_order = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['sort_order', 'name']
        verbose_name = 'Festival'
        verbose_name_plural = 'Festivals'

    def __str__(self):
        return f'{self.name} — {self.city}'
