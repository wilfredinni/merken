from django.urls import reverse, resolve
from django.test import TestCase
from ..views import article
from ..models import Article, CustomUser


class ArticleTest(TestCase):

    def setUp(self):
        user = CustomUser.objects.create_user("test_user")
        Article.objects.create(url="test-article", author=user)

    def test_article_view_status_code(self):
        url = reverse("blog_app:article", kwargs={"url": "test-article"})
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200)

    def test_url_resolves_article_view(self):
        view = resolve("/blog/test-article/")
        self.assertEquals(view.func, article)

    def test_article_view_not_found_404(self):
        url = reverse('blog_app:article', kwargs={'url': 'wrong-url'})
        response = self.client.get(url)
        self.assertEquals(response.status_code, 404)
