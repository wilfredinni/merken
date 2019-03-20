from django.db import models

from solo.models import SingletonModel


class SiteConfiguration(SingletonModel):
    site_name = models.CharField(max_length=120, default="Site Name")
    site_description = models.TextField(default='Website description.')
    canonical_url = models.CharField(max_length=120, default='www.mysite.com')
    publisher = models.CharField(max_length=120, default='Publisher')
    email = models.EmailField(max_length=120, default='my@email.com')

    # TODO: haven't decided how to load this images... add fields for twitter cards!!
    favicon = models.CharField(max_length=120, default='some url for now')
    site_img = models.CharField(max_length=120, default='some url for now')

    class Meta:
        verbose_name = "Site Configuration"
