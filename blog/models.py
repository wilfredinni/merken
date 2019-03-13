from django.db import models
from django.utils import timezone
from django.urls import reverse

from users.models import CustomUser


class Tag(models.Model):
    title = models.SlugField(unique=True)

    def get_absolute_url(self):
        return reverse('blog_app:tag', kwargs={'tag_name': self.title})

    def __str__(self):
        return self.title


class Article(models.Model):
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    title = models.CharField(max_length=120, unique=True)
    overview = models.TextField()
    content = models.TextField()
    img_url = models.CharField(max_length=200)
    tags = models.ManyToManyField(Tag)
    featured = models.BooleanField(default=False)
    url = models.SlugField(max_length=120, unique=True)
    created_at = models.DateTimeField(default=timezone.now)

    def get_absolute_url(self):
        return reverse('blog_app:article', kwargs={'url': self.url})

    def __str__(self):
        return self.title

    class Meta:
        ordering = ["-created_at"]
