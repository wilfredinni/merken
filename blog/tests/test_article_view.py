from django.test import TestCase
from django.urls import reverse, resolve

from ..views import ArticleView
from ..models import Article, CustomUser


class ArticleTest(TestCase):

    def setUp(self):
        user = CustomUser.objects.create_user("test_user")
        Article.objects.create(url="test-article", author=user)

    def test_article_view_status_code(self):
        url = reverse("blog_app:article", kwargs={"slug": "test-article"})
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200)

    def test_article_view_not_found_404(self):
        url = reverse('blog_app:article', kwargs={'slug': 'wrong-url'})
        response = self.client.get(url)
        self.assertEquals(response.status_code, 404)

    def test_url_resolves_article_view(self):
        view = resolve("/blog/test-article/")
        self.assertEquals(view.func.view_class, ArticleView)
