from django.db import models
from django.utils import timezone


class Page(models.Model):
    title = models.CharField(max_length=120, unique=True)
    overview = models.TextField()
    content = models.TextField()
    url = models.SlugField(max_length=120, unique=True)
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title
