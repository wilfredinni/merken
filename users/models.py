from django.contrib.auth.models import AbstractUser

from django.urls import reverse
from django.db import models


class CustomUser(AbstractUser):
    twitter = models.CharField(max_length=120, blank=True)
    github = models.CharField(max_length=120, blank=True)
    website = models.CharField(max_length=120, blank=True)
    about = models.TextField(blank=True)

    def get_absolute_url(self):
        return reverse("users_app:profile", kwargs={"slug": self.username})

    def __str__(self):
        return self.username

    class Meta:
        ordering = ["username"]
