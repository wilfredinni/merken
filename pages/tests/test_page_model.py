from django.test import TestCase
from ..models import Page


class PageModel(TestCase):
    def setUp(self):
        Page.objects.create(
            title="title",
            overview="overview",
            content="content",
            url="url"
        )

    def test_pages_model(self):
        page = Page.objects.get(url="url")
        self.assertEqual(page.title, "title")
        self.assertEqual(page.overview, "overview")
        self.assertEqual(page.content, "content")
        self.assertEqual(page.url, "url")
