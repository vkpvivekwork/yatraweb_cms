from django.db import models


class GalleryPhoto(models.Model):

    FILE_TYPE_CHOICES = [
        ('image', 'Image'),
        ('video', 'Video'),
    ]

    CATEGORY_CHOICES = [
        ('ghats',     'Ghats'),
        ('aarti',     'Aarti'),
        ('boats',     'Boats'),
        ('temples',   'Temples'),
        ('festivals', 'Festivals'),
        ('food',      'Food'),
        ('other',     'Other'),
    ]

    SEASON_CHOICES = [
        ('any',      'Any'),
        ('winter',   'Winter'),
        ('summer',   'Summer'),
        ('monsoon',  'Monsoon'),
        ('festive',  'Festive'),
    ]

    SECTION_CHOICES = [
        ('all',          'All'),
        ('ribbon',       'Ribbon'),
        ('gallery',      'Gallery'),
        ('footer_strip', 'Footer Strip'),
    ]

    SOURCE_CHOICES = [
        ('unsplash', 'Unsplash'),
        ('own',      'Own'),
        ('client',   'Client'),
        ('stock',    'Stock'),
    ]

    # Identity
    title           = models.CharField(max_length=200, blank=True)

    # Media
    image_url       = models.CharField(max_length=500)
    thumbnail_url   = models.CharField(max_length=500, blank=True)
    file_type       = models.CharField(max_length=10, choices=FILE_TYPE_CHOICES, default='image')
    video_url       = models.CharField(max_length=500, blank=True)
    width           = models.PositiveIntegerField(null=True, blank=True)
    height          = models.PositiveIntegerField(null=True, blank=True)

    # Content
    alt_text        = models.CharField(max_length=300)
    caption         = models.CharField(max_length=300, blank=True)
    description     = models.TextField(blank=True)

    # Classification
    category        = models.CharField(max_length=50, choices=CATEGORY_CHOICES, blank=True)
    tags            = models.JSONField(default=list, blank=True)
    location        = models.CharField(max_length=200, blank=True)
    season          = models.CharField(max_length=20, choices=SEASON_CHOICES, default='any')
    section         = models.CharField(max_length=20, choices=SECTION_CHOICES, default='all')

    # Source
    source          = models.CharField(max_length=20, choices=SOURCE_CHOICES, default='unsplash')
    photographer    = models.CharField(max_length=200, blank=True)
    source_url      = models.CharField(max_length=500, blank=True)
    taken_on        = models.DateField(null=True, blank=True)

    # Relations
    linked_packages = models.ManyToManyField(
        'packages.Package',
        blank=True,
        related_name='gallery_photos',
    )

    # Control
    is_active       = models.BooleanField(default=True)
    is_featured     = models.BooleanField(default=False)
    sort_order      = models.PositiveIntegerField(default=0)
    created_at      = models.DateTimeField(auto_now_add=True)
    updated_at      = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['sort_order', '-created_at']
        verbose_name = 'Gallery Photo'
        verbose_name_plural = 'Gallery Photos'

    def __str__(self):
        return self.title or self.caption or f'Photo {self.pk}'
