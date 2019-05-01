from django.contrib.syndication.views import Feed

from dashboard.models import SiteConfiguration
from .models import Article

from mistune import markdown


class ArticleFeed(Feed):
    try:
        site_info = SiteConfiguration.load()
    except:
        pass

    link = "/blog/"
    description = (  # replace with SiteConfiguration
        f"Updates to the Python Cheatsheet Blog"
    )

    def title(self):
        return f"{self.site_info.site_name}"

    def items(self):
        return Article.objects.all()[:20]

    def item_title(self, item):
        return item.title

    def item_description(self, item):
        return markdown(item.overview)
