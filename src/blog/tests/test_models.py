from django.test import TestCase
from ..models import CustomUser, Article, Tag


class TestModels(TestCase):
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

        self.article = Article.objects.get(url="url")
        self.tag = Tag.objects.get(title="test_tag")

    def test_article_model(self):
        self.assertEqual(self.article.author.username, "test_user")
        self.assertEqual(self.article.title, "title")
        self.assertEqual(self.article.overview, "overview")
        self.assertEqual(self.article.content, "content")
        self.assertEqual(self.article.img_url, "img_url")
        self.assertEqual(self.article.featured, False)
        self.assertEqual(self.article.url, "url")

    def test_tag_model(self):
        self.assertEqual(self.tag.title, "test_tag")

    def test_append_tag(self):
        self.article.tags.add(self.tag)
        self.assertEqual(self.article.tags.first(), self.tag)

    def test_remove_tag(self):
        self.article.tags.add(self.tag)
        self.article.tags.remove(self.tag)
        self.assertNotEqual(self.article.tags.first(), self.tag)
