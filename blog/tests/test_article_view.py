from django.urls import reverse, resolve
from django.test import TestCase
from ..views import article


class HomeTests(TestCase):

    def test_article_view_status_code(self):
        url = reverse("blog_app:article")
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200)

    def test_url_resolves_article_view(self):
        view = resolve("/blog/article/")
        self.assertEquals(view.func, article)
