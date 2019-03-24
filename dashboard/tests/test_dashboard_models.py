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

    def test_site_configuration_model(self):
        config = SiteConfiguration.objects.get()
        self.assertEqual(config.site_name, "site_name")
        self.assertEqual(config.site_description, "description")
        self.assertEqual(config.canonical_url, "https://www.site.com")
        self.assertEqual(config.publisher, "author")
        self.assertEqual(config.email, "my@email.com")
        self.assertEqual(config.favicon, "path/to/favicon.png")
        self.assertEqual(config.site_img, "pat/to/img.png")


class HomeMsgModel(TestCase):
    def setUp(self):
        HomeMsg.objects.create(content="content", enabled=True)

    def test_home_msg_model(self):
        message = HomeMsg.objects.get()
        self.assertEqual(message.content, 'content')
        self.assertEqual(message.enabled, True)
