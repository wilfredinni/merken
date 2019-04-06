from django.db import models
from django.core.cache import cache


class SingletonModel(models.Model):
    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        self.pk = 1
        super(SingletonModel, self).save(*args, **kwargs)
        self.set_cache()

    def delete(self, *args, **kwargs):
        pass

    @classmethod
    def load(cls):
        if cache.get(cls.__name__) is None:
            obj, created = cls.objects.get_or_create(pk=1)
            if not created:
                obj.set_cache()

        return cache.get(cls.__name__)

    def set_cache(self):
        cache.set(self.__class__.__name__, self)


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

    # blog (not working yet)
    posts_per_page = models.IntegerField(default=5)

    # others
    enable_ads = models.BooleanField(default=False)
    enable_analytics = models.BooleanField(default=False)

    class Meta:
        verbose_name = "Site Configuration"


class HomeMsg(SingletonModel):
    content = models.TextField(null=True, blank=True)
    enabled = models.BooleanField(default=False)

    class Meta:
        verbose_name = "Home Message"
