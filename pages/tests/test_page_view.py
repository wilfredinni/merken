from django.test import TestCase
from django.urls import reverse, resolve

from ..views import PageView
from ..models import Page


class PageTest(TestCase):
    def setUp(self):
        Page.objects.create(url="test_page")

    def test_page_view_status_code(self):
        url = reverse("page_app:page", kwargs={"slug": "test_page"})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_page_view_not_fount_404(self):
        url = reverse("page_app:page", kwargs={"slug": "wrong_page"})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 404)

    def test_url_resolves_page_view(self):
        view = resolve('/test_page/')
        self.assertEqual(view.func.view_class, PageView)
