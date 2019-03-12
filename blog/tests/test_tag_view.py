from django.urls import reverse, resolve
from django.test import TestCase
from ..views import article_by_tag


class HomeTests(TestCase):
    def test_article_by_tag_view_status_code(self):
        url = reverse("blog_app:tag")
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200)

    def test_url_resolves_article_by_tag_view(self):
        view = resolve("/blog/tag/")
        self.assertEquals(view.func, article_by_tag)
