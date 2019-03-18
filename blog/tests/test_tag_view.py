from django.urls import reverse, resolve
from django.test import TestCase
from ..views import TagView
from ..models import Tag


class HomeTests(TestCase):
    def setUp(self):
        # user = User.objects.create_user("test_user")
        Tag.objects.create(title="python")

    def test_article_view_status_code(self):
        url = reverse("blog_app:tag", kwargs={"slug": "python"})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_url_resolves_article_by_tag_view(self):
        view = resolve("/blog/tag/python/")
        self.assertEqual(view.func.view_class, TagView)

    def test_tag_view_not_found_404(self):
        url = reverse('blog_app:tag', kwargs={'slug': 'wrong-tag'})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 404)
