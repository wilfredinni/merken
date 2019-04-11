from django.test import TestCase
from ..models import Page


class PageModelDefaults(TestCase):
    def setUp(self):
        Page.objects.create(
            title="title",
            overview="overview",
            content="content",
            url="url"
        )

        self.page = Page.objects.get(url="url")

    def test_pages_model_defaults(self):
        self.assertEqual(self.page.title, "title")
        self.assertEqual(self.page.overview, "overview")
        self.assertEqual(self.page.content, "content")
        self.assertEqual(self.page.url, "url")

        # defaults
        self.assertEqual(self.page.visible, False)
        self.assertEqual(self.page.order, 0)

    def test_pages_default_modified(self):
        self.page.visible = True
        self.page.order = 1
        self.page.save()
        self.assertEqual(self.page.visible, True)
        self.assertEqual(self.page.order, 1)
