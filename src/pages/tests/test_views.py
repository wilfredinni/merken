from django.test import TestCase, Client
from django.urls import reverse

from ..models import Page


class TestPageView(TestCase):
    def setUp(self):
        self.client = Client()
        Page.objects.create(url="test_slug")

    def test_page_GET(self):
        url = reverse("page_app:page", args=["test_slug"])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "pages/page.html")

    def test_page_404(self):
        url = reverse("page_app:page", args=["wrong_page"])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 404)


class TestIndexView(TestCase):
    def setUp(self):
        self.client = Client()

    def test_index_GET(self):
        Page.objects.create(url="index")
        url = reverse("page_app:index")
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "pages/index.html")

    def test_index_404(self):
        url = reverse("page_app:index")
        response = self.client.get(url)
        self.assertEqual(response.status_code, 404)
