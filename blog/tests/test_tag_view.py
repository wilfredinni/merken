from django.urls import reverse, resolve
from django.test import TestCase
from ..views import article_by_tag
from ..models import Tag


class HomeTests(TestCase):
    def setUp(self):
        # user = User.objects.create_user("test_user")
        Tag.objects.create(title="python")

    def test_article_view_status_code(self):
        url = reverse("blog_app:tag", kwargs={"tag_name": "python"})
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200)

    def test_url_resolves_article_by_tag_view(self):
        view = resolve("/blog/tag/python/")
        self.assertEquals(view.func, article_by_tag)
