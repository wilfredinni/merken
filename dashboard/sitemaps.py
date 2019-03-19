from django.contrib.sitemaps import Sitemap
from django.shortcuts import reverse

# from blog.models import Article, Tag
# from pages.models import Page


class StaticViewSitemap(Sitemap):
    def items(self):
        return ["blog_app:blog"]

    def location(self, item):
        return reverse(item)


# class ArticleSitemap(Sitemap):
#     def item(self):
#         return Article.objects.all()


# class TagSitemap(Sitemap):
#     def item(self):
#         print('tags')
#         return Tag.objects.all()


# class PageSitemap(Sitemap):
#     def item(self):
#         return Page.objects.all()
