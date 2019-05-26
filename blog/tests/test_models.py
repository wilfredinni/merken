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
            content="content",
            slug="url",
            img_url="img_url",
        )

        self.article = Article.objects.get(slug="url")
        self.tag = Tag.objects.get(title="test_tag")

    def test_str(self):
        self.assertEqual(str(self.article), "title")

    def test_article_model_defaults(self):
        self.assertEqual(self.article.author.username, "test_user")
        self.assertEqual(self.article.title, "title")
        self.assertEqual(self.article.overview, "overview")
        self.assertEqual(self.article.content, "content")
        self.assertEqual(self.article.img_url, "img_url")
        self.assertEqual(self.article.slug, "url")

        # defaults
        self.assertEqual(self.article.is_featured, False)
        self.assertEqual(self.article.is_draft, False)
        self.assertEqual(self.article.allow_comments, True)

    def test_article_model_modified(self):
        self.article.is_featured = True
        self.article.is_draft = True
        self.article.allow_comments = False
        self.article.save()
        self.assertEqual(self.article.is_featured, True)
        self.assertEqual(self.article.is_draft, True)
        self.assertEqual(self.article.allow_comments, False)

    def test_tag_model(self):
        self.assertEqual(self.tag.title, "test_tag")

    def test_append_tag(self):
        self.article.tags.add(self.tag)
        self.assertEqual(self.article.tags.first(), self.tag)

    def test_remove_tag(self):
        self.article.tags.add(self.tag)
        self.article.tags.remove(self.tag)
        self.assertNotEqual(self.article.tags.first(), self.tag)


class TestManagers(TestCase):
    def setUp(self):
        posts = [
            ["title1", True, True, "url1"],
            ["title2", False, False, "url2"],
            ["title3", False, True, "url3"],
            ["title4", True, False, "url4"],
        ]
        user = CustomUser.objects.create_user("test_user")
        for post in posts:
            Article.objects.create(
                author=user,
                title=post[0],
                is_draft=post[1],
                is_featured=post[2],
                slug=post[3],
            )

    def test_featured_published(self):
        queryset = Article.objects.all()
        self.assertEqual(len(queryset.featured()), 2)
        self.assertEqual(len(queryset.published()), 2)
