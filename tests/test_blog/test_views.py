from django.test import TestCase, Client
from django.urls import reverse

from apps.users.models import CustomUser
from apps.blog.models import Article, Tag


class TestBlogView(TestCase):
    def setUp(self):
        self.client = Client()

    def test_blog_GET(self):
        url = reverse("blog_app:blog")
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "merken/blog/blog.html")


class TestArticleView(TestCase):
    def setUp(self):
        self.client = Client()
        user = CustomUser.objects.create_user("test_user")
        Article.objects.create(slug="test_slug", author=user)

    def test_article_GET(self):
        url = reverse("blog_app:article", args=["test_slug"])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "merken/blog/article.html")

    def test_article_404(self):
        url = reverse("blog_app:article", args=["wrong_slug"])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 404)


class TestTagView(TestCase):
    def setUp(self):
        self.client = Client()
        Tag.objects.create(title="python")

    def test_tag_GET(self):
        url = reverse("blog_app:tag", args=["python"])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "merken/blog/blog.html")

    def test_tag_404(self):
        url = reverse("blog_app:tag", args=["wrong-tag"])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 404)


class TestRssFeed(TestCase):
    def setUp(self):
        self.client = Client()

    def test_feed_GET(self):
        url = reverse("blog_app:rss_feed")
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
