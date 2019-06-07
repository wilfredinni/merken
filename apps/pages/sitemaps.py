from django.contrib.sitemaps import Sitemap
from .models import Page


class PagesSitemap(Sitemap):
    protocol = "https"
    changefreq = "weekly"
    priority = 0.9

    def items(self):
        # TODO filter for visible pages (bool) whitout descarting index
        return Page.objects.all()

    def lastmod(self, obj):
        return obj.created_at
