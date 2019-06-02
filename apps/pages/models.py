from django.db import models
from django.utils import timezone
from django.urls import reverse


class Page(models.Model):
    title = models.CharField(max_length=120, unique=True)
    overview = models.TextField()
    content = models.TextField()
    slug = models.SlugField(max_length=120, unique=True)
    visible = models.BooleanField(default=False)
    order = models.IntegerField(default=0)
    created_at = models.DateTimeField(default=timezone.now)

    def get_absolute_url(self):
        return reverse("page_app:page", kwargs={"slug": self.slug})

    def __str__(self):
        return self.title

    class Meta:
        ordering = ["order"]
