from django.contrib.syndication.views import Feed

from .models import Article

from dashboard.models import SiteConfiguration


class ArticleFeed(Feed):
    # site_info = SiteConfiguration.load()

    # title = f"{site_info.site_name} Blog Feed"
    # link = "/blog/"
    # description = f"Updates to the {site_info.site_name} Blog"

    # def items(self):
    #     return Article.objects.all()[:5]

    # def item_title(self, item):
    #     return item.title

    # def item_description(self, item):
    #     return item.overview
    pass
