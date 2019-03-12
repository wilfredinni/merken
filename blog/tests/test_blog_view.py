from django.urls import reverse, resolve
from django.test import TestCase

from ..views import blog


class BlogView(TestCase):
    def test_blog_view_status_code(self):
        url = reverse("blog_app:blog")
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200)

    def test_url_resolves_blog_view(self):
        view = resolve("/blog/")
        self.assertEquals(view.func, blog)
