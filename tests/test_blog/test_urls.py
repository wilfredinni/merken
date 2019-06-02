from django.test import SimpleTestCase
from django.urls import reverse, resolve

from apps.blog.views import ArticleView, BlogView, TagView


class TestUrls(SimpleTestCase):
    def test_blog_url_resolves(self):
        url = reverse("blog_app:blog")
        self.assertEqual(resolve(url).func.view_class, BlogView)

    def test_article_url_resolves(self):
        url = reverse("blog_app:article", args=["test-article"])
        self.assertEqual(resolve(url).func.view_class, ArticleView)

    def test_tag_url_resolves(self):
        url = reverse("blog_app:tag", args=["python"])
        self.assertEqual(resolve(url).func.view_class, TagView)
