from django.test import TestCase
from ..models import CustomUser, Article, Tag


class BlogModels(TestCase):
    def setUp(self):
        user = CustomUser.objects.create_user("test_user")
        Tag.objects.create(title="test_tag")
        Article.objects.create(
            author=user,
            title="title",
            overview="overview",
            content='content',
            url="url",
            img_url='img_url'
        )

    def test_article_model(self):
        article = Article.objects.get(url="url")
        self.assertEqual(article.author.username, "test_user")
        self.assertEqual(article.title, "title")
        self.assertEqual(article.overview, "overview")
        self.assertEqual(article.content, "content")
        self.assertEqual(article.img_url, "img_url")
        self.assertEqual(article.featured, False)
        self.assertEqual(article.url, "url")

    def test_tag_model(self):
        tag = Tag.objects.get(title="test_tag")
        self.assertEqual(tag.title, "test_tag")

    def test_append_tag(self):
        article = Article.objects.get(url="url")
        tag = Tag.objects.get(title="test_tag")
        article.tags.add(tag)
        self.assertEqual(article.tags.first(), tag)

    def test_remove_tag(self):
        article = Article.objects.get(url="url")
        tag = Tag.objects.get(title="test_tag")
        article.tags.add(tag)
        article.tags.remove(tag)
        self.assertNotEqual(article.tags.first(), tag)
