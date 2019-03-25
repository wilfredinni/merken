from django.test import TestCase
from ..models import SiteConfiguration, HomeMsg


class SiteConfigurationModel(TestCase):
    def setUp(self):
        SiteConfiguration.objects.create(
            site_name="site_name",
            site_description="description",
            canonical_url="https://www.site.com",
            publisher="author",
            email="my@email.com",
            # from here is incomplete, but the tests will pass anyway
            favicon="path/to/favicon.png",
            site_img="pat/to/img.png",
        )
        self.config = SiteConfiguration.objects.get()

    def test_site_configuration_model(self):
        self.assertEqual(self.config.site_name, "site_name")
        self.assertEqual(self.config.site_description, "description")
        self.assertEqual(self.config.canonical_url, "https://www.site.com")
        self.assertEqual(self.config.publisher, "author")
        self.assertEqual(self.config.email, "my@email.com")
        self.assertEqual(self.config.favicon, "path/to/favicon.png")
        self.assertEqual(self.config.site_img, "pat/to/img.png")


class HomeMsgModel(TestCase):
    def setUp(self):
        HomeMsg.objects.create(content="content", enabled=True)
        self.message = HomeMsg.objects.get()

    def test_home_msg_model(self):
        self.assertEqual(self.message.content, "content")
        self.assertEqual(self.message.enabled, True)
