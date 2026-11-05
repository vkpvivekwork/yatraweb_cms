from django.db import models


class Package(models.Model):
    id = models.SlugField(primary_key=True, max_length=100)
    title = models.CharField(max_length=200)
    subtitle = models.CharField(max_length=300, blank=True)
    duration = models.CharField(max_length=100)
    cities = models.JSONField(default=list)
    starting_price = models.CharField(max_length=50, blank=True, null=True)
    hero_img = models.CharField(max_length=200, blank=True)
    img_alt = models.CharField(max_length=300, blank=True)

    # homepage card
    features = models.JSONField(default=list)      # 4 bullet points shown on card
    pkg_label = models.CharField(max_length=200, blank=True)  # text used in booking form dropdown

    # detail page
    places = models.JSONField(default=list)        # temples, stupas, forts, museums, ghats, etc.
    activities = models.JSONField(default=list)    # Ganga Aarti, Sunrise Boat Ride, etc.
    inclusions = models.JSONField(default=list)
    exclusions = models.JSONField(default=list)

    # meta
    is_popular = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    order = models.PositiveIntegerField(default=0, help_text='Display order on listing page')
    min_duration_days = models.PositiveIntegerField(null=True, blank=True)
    min_group = models.CharField(max_length=100, blank=True, null=True)
    tags = models.JSONField(default=list)          # e.g. ['spiritual', 'group', 'budget']
    meta_description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['order', 'created_at']

    def __str__(self):
        return self.title


class PackageDay(models.Model):
    package = models.ForeignKey(Package, related_name='days', on_delete=models.CASCADE)
    order = models.PositiveIntegerField(default=0)
    day = models.CharField(max_length=20)          # "Day 01", "Day 1"
    city = models.CharField(max_length=100, blank=True, null=True)
    title = models.CharField(max_length=200)
    activities = models.JSONField(default=list)
    stay = models.CharField(max_length=100, blank=True, null=True)
    meals = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return f'{self.package.title} — {self.day}: {self.title}'


class PackagePricing(models.Model):
    package = models.ForeignKey(Package, related_name='pricing', on_delete=models.CASCADE)
    order = models.PositiveIntegerField(default=0)
    group = models.CharField(max_length=100)       # "2 persons", "4 Pax"
    rate = models.CharField(max_length=50)         # "₹9,500"
    vehicle = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return f'{self.package.title} — {self.group}: {self.rate}'
