from django.contrib.syndication.views import Feed

from .models import Article

# TODO: error when loading siteconfiguration, load settings form
# SiteConfiguration
# from dashboard.models import SiteConfiguration


class ArticleFeed(Feed):
    # site_info = SiteConfiguration.objects.get(pk=1)

    title = f"Python Cheatsheet Blog Feed"  # replace with SiteConfiguration
    link = "/blog/"
    description = (  # replace with SiteConfiguration
        f"Updates to the Python Cheatsheet Blog"
    )

    def items(self):
        return Article.objects.all()[:5]

    def item_title(self, item):
        return item.title

    def item_description(self, item):
        return item.overview

    pass
