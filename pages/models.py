from django.db import models
from django.utils import timezone
from django.urls import reverse


class Page(models.Model):
    title = models.CharField(max_length=120, unique=True)
    overview = models.TextField()
    content = models.TextField()
    url = models.SlugField(max_length=120, unique=True)
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("pages_app:page", kwargs={"slug": self.url})
