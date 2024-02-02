from django.db import models
from datetime import datetime
from .utils import generate_random_string


class ShortenedUrl(models.Model):
    url = models.URLField(null=True, blank=True)
    shortcode = models.CharField(max_length=6, unique=True, null=True, blank=True)

    created = models.DateTimeField(auto_now=True)
    last_redirect = models.DateTimeField(null=True, blank=True)

    redirect_count = models.IntegerField(default=0, null=True, blank=True)

    def __str__(self):
        return f'{self.url} : {self.shortcode}'

    def save(self, *args, **kwargs):
        if self.shortcode is None:
            self.create_short_code()
        super(ShortenedUrl, self).save(*args, **kwargs)

    def create_short_code(self):
        self.shortcode = generate_random_string()
        # Handling potential random duplicates
        if ShortenedUrl.objects.filter(shortcode=self.shortcode).exists():
            self.create_short_code()

    def increment_redirect_count(self):
        self.redirect_count += 1
        self.save()

    def set_last_redirect(self):
        self.last_redirect = datetime.now()
        self.save()

    def update_url_stats(self):
        self.increment_redirect_count()
        self.set_last_redirect()

    class Meta:
        verbose_name = "Shortened Url"
        verbose_name_plural = "Shortened Urls"
