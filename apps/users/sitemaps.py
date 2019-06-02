from django.contrib.sitemaps import Sitemap
from .models import CustomUser


class UsersSitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.9

    def items(self):
        return CustomUser.objects.all()
