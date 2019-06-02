from django.test import TestCase, Client
from django.urls import reverse


class TestBlogView(TestCase):
    def setUp(self):
        self.client = Client()

    def test_blog_GET(self):
        url = reverse("django.contrib.sitemaps.views.sitemap")
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
