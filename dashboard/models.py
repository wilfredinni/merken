from django.db import models


class SingletonModel(models.Model):
    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        self.pk = 1
        super(SingletonModel, self).save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        pass

    @classmethod
    def load(cls):
        obj, created = cls.objects.get_or_create(pk=1)
        return obj


class SiteConfiguration(SingletonModel):
    site_name = models.CharField(max_length=120, default="Site Name")
    site_description = models.TextField(default="Website description.")
    canonical_url = models.CharField(max_length=120, default="www.mysite.com")
    publisher = models.CharField(max_length=120, default="Publisher")
    email = models.EmailField(max_length=120, default="my@email.com")

    # TODO: haven't decided how to load this images...
    # add fields for twitter cards!!
    favicon = models.CharField(max_length=120, default="some url for now")
    site_img = models.CharField(max_length=120, default="some url for now")

    # switches
    enable_ads = models.BooleanField(default=False)
    enable_analytics = models.BooleanField(default=False)

    class Meta:
        verbose_name = "Site Configuration"

    def __str__(self):
        return self.site_name


class HomeMsg(SingletonModel):
    content = models.TextField(null=True, blank=True)
    enabled = models.BooleanField(default=False)

    class Meta:
        verbose_name = "Home Message"
