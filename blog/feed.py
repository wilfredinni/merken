from django.contrib.syndication.views import Feed
from mistune import markdown

from .models import Article


class ArticleFeed(Feed):
    link = "/blog/"
    description = (
        f"Updates to the Python Cheatsheet Blog"
    )

    def title(self):
        return "Python Cheatsheet"

    def items(self):
        return Article.objects.all()[:20]

    def item_title(self, item):
        return item.title

    def item_description(self, item):
        return markdown(item.content)
