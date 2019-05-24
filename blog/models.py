from django.db import models
from django.utils import timezone
from django.urls import reverse

from users.models import CustomUser


class ArticleQuerySet(models.QuerySet):
    """
    Custom model manager for Articles
    """

    def published(self):
        return self.filter(is_draft=False, created_at__lte=timezone.now())

    def featured(self):
        return self.filter(is_featured=True)


class Tag(models.Model):
    title = models.SlugField(unique=True)

    def get_absolute_url(self):
        return reverse("blog_app:tag", kwargs={"slug": self.title})

    def __str__(self):
        return self.title

    class Meta:
        ordering = ["-id"]


class Article(models.Model):
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    title = models.CharField(max_length=120, unique=True)
    overview = models.TextField()
    content = models.TextField()
    img_url = models.CharField(max_length=200)
    tags = models.ManyToManyField(Tag)
    url = models.SlugField(max_length=120, unique=True)
    is_draft = models.BooleanField(default=False)
    allow_comments = models.BooleanField(default=True)
    is_featured = models.BooleanField(default=False)
    created_at = models.DateTimeField(default=timezone.now)

    # use ArticleQuerySet as the manager for this model
    objects = ArticleQuerySet.as_manager()

    def get_absolute_url(self):
        return reverse("blog_app:article", kwargs={"slug": self.url})

    @property
    def is_in_past(self):
        return self.created_at < timezone.now()

    def __str__(self):
        return self.title

    class Meta:
        ordering = ["-created_at"]
