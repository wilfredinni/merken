from django.test import SimpleTestCase
from django.urls import reverse, resolve

from ..views import PageView, IndexView


class TestUrls(SimpleTestCase):
    def test_page_url_resolves(self):
        url = reverse("page_app:page", args=["test_slug"])
        self.assertEqual(resolve(url).func.view_class, PageView)

    def test_url_resolves_page_view(self):
        url = reverse("page_app:index")
        self.assertEqual(resolve(url).func.view_class, IndexView)
