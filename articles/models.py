from django.db import models


class ArticleCategory(models.Model):
    name        = models.CharField(max_length=100)
    slug        = models.SlugField(unique=True)
    description = models.CharField(max_length=300, blank=True)
    image_url   = models.CharField(max_length=500, blank=True)
    sort_order  = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['sort_order', 'name']
        verbose_name = 'Article Category'
        verbose_name_plural = 'Article Categories'

    def __str__(self):
        return self.name


class Article(models.Model):

    CONTENT_TYPE_CHOICES = [
        ('guide',      'Guide'),
        ('story',      'Story'),
        ('tips',       'Tips'),
        ('itinerary',  'Itinerary'),
        ('festival',   'Festival'),
    ]

    ARTICLE_TYPE_CHOICES = [
        ('guides',       'Guides'),
        ('journal',      'Journal'),
        ('safarnama',    'Safarnama'),
        ('insights',     'Insights'),
        ('itineraries',  'Itineraries'),
    ]

    SEASON_CHOICES = [
        ('any',      'Any'),
        ('winter',   'Winter'),
        ('summer',   'Summer'),
        ('monsoon',  'Monsoon'),
        ('festive',  'Festive'),
    ]

    STATUS_CHOICES = [
        ('draft',     'Draft'),
        ('published', 'Published'),
        ('archived',  'Archived'),
    ]

    # ── Identity ──────────────────────────────────────────────────────────────
    title = models.CharField(max_length=300)
    slug  = models.SlugField(unique=True, max_length=350)

    # ── Content ───────────────────────────────────────────────────────────────
    excerpt          = models.TextField()
    body             = models.TextField()
    featured_image   = models.CharField(max_length=500, blank=True)
    featured_image_alt = models.CharField(max_length=300, blank=True)

    # ── Classification ────────────────────────────────────────────────────────
    category     = models.ForeignKey(
        ArticleCategory,
        null=True, blank=True,
        on_delete=models.SET_NULL,
        related_name='articles',
    )
    content_type = models.CharField(max_length=20, choices=CONTENT_TYPE_CHOICES, default='guide')
    article_type = models.CharField(max_length=20, choices=ARTICLE_TYPE_CHOICES, default='guides')

    # ── Travel Context ────────────────────────────────────────────────────────
    destinations     = models.JSONField(default=list, blank=True)
    season           = models.CharField(max_length=20, choices=SEASON_CHOICES, default='any', blank=True)
    related_packages = models.ManyToManyField(
        'packages.Package',
        blank=True,
        related_name='articles',
    )

    # ── SEO ───────────────────────────────────────────────────────────────────
    meta_title         = models.CharField(max_length=200, blank=True)
    meta_description   = models.TextField(blank=True)
    og_image_url       = models.CharField(max_length=500, blank=True)
    canonical_url      = models.CharField(max_length=500, blank=True)
    primary_keyword    = models.CharField(max_length=200, blank=True)
    secondary_keywords = models.JSONField(default=list, blank=True)

    # ── Publishing ────────────────────────────────────────────────────────────
    status       = models.CharField(max_length=20, choices=STATUS_CHOICES, default='draft')
    published_at = models.DateTimeField(null=True, blank=True)
    is_featured  = models.BooleanField(default=False)
    sort_order   = models.PositiveIntegerField(default=0)

    # ── Control ───────────────────────────────────────────────────────────────
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['sort_order', '-published_at']
        verbose_name = 'Article'
        verbose_name_plural = 'Articles'

    def __str__(self):
        return self.title
