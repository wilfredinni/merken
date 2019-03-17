from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    twitter = models.CharField(max_length=120, blank=True)
    github = models.CharField(max_length=120, blank=True)
    website = models.CharField(max_length=120, blank=True)
    about = models.TextField(blank=True)

    def __str__(self):
        return self.username
