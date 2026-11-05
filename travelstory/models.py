from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models


class TravelStory(models.Model):

    # Guest Info
    name = models.CharField(max_length=200)
    hometown = models.CharField(max_length=200, blank=True)
    mobile = models.CharField(max_length=20, blank=True, help_text='Internal only — not exposed in public API')
    travel_type = models.CharField(max_length=100, blank=True, help_text='e.g. Solo, Couple, Family, Group, Honeymoon, Corporate')

    # Trip Details
    package = models.ForeignKey(
        'packages.Package',
        null=True, blank=True,
        on_delete=models.SET_NULL,
        related_name='travel_stories',
    )
    places_visited = models.JSONField(default=list, blank=True)
    services_used = models.JSONField(default=list, blank=True)
    num_people = models.PositiveIntegerField(null=True, blank=True)
    start_date = models.DateField(null=True, blank=True)
    end_date = models.DateField(null=True, blank=True)

    # Their Story
    highlight_quote = models.CharField(max_length=300, blank=True, help_text='Bold one-liner shown on the testimonial card')
    testimonial = models.TextField(blank=True, help_text='Full review text')
    rating = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)],
        null=True, blank=True,
    )

    # Media
    featured_image = models.CharField(max_length=500, blank=True, help_text='Testimonial card image URL')
    testimonial_video_url = models.CharField(max_length=500, blank=True, help_text='YouTube / Reels / WhatsApp video link')
    testimonial_thumbnail = models.CharField(max_length=500, blank=True, help_text='Custom preview image for the video')
    social_post_url = models.CharField(max_length=500, blank=True, help_text='Their Instagram / Facebook / YouTube post about the trip')
    google_review_link = models.CharField(max_length=500, blank=True, help_text='Their Google Maps review link')

    # Internal / Marketing
    booking_source = models.CharField(max_length=100, blank=True, help_text='e.g. Google Search, Instagram, WhatsApp, Referral, Walk-in, Facebook Ads')

    # Control
    is_featured = models.BooleanField(default=False, help_text='Show on homepage')
    is_approved = models.BooleanField(default=False, help_text='Only approved stories are public')
    order = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['order', '-created_at']
        verbose_name = 'Travel Story'
        verbose_name_plural = 'Travel Stories'

    def __str__(self):
        return f'{self.name} — {self.travel_type} ({self.start_date or "date unknown"})'

    @property
    def num_days(self):
        if self.start_date and self.end_date:
            return (self.end_date - self.start_date).days + 1
        return None


class TravelStoryPhoto(models.Model):
    story = models.ForeignKey(TravelStory, related_name='photos', on_delete=models.CASCADE)
    image_url = models.CharField(max_length=500)
    caption = models.CharField(max_length=300, blank=True)
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return f'{self.story.name} — photo {self.order}'
