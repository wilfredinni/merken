from django.test import TestCase
from ..models import SiteConfiguration, HomeMsg


class SiteConfigurationModelDefaults(TestCase):
    def setUp(self):
        self.config = SiteConfiguration.load()

    def test_site_configuration_model_defaults(self):
        self.assertEqual(self.config.site_name, "Site Name")
        self.assertEqual(self.config.site_description, "Website description.")
        self.assertEqual(self.config.canonical_url, "www.mysite.com")
        self.assertEqual(self.config.publisher, "Publisher")
        self.assertEqual(self.config.email, "my@email.com")
        self.assertEqual(self.config.favicon, "some url for now")
        self.assertEqual(self.config.site_img, "some url for now")
        self.assertEqual(self.config.enable_ads, False)
        self.assertEqual(self.config.enable_analytics, False)


class SiteConfigurationModelModified(TestCase):
    def setUp(self):
        SiteConfiguration.objects.create(
            site_name="site_name",
            site_description="description",
            canonical_url="https://www.site.com",
            publisher="author",
            email="my@email.org",
            favicon="path/to/favicon.png",
            site_img="pat/to/img.png",
            enable_ads=True,
            enable_analytics=True,
        )
        self.config = SiteConfiguration.objects.get()

    def test_site_configuration_model_modified(self):
        self.assertEqual(self.config.site_name, "site_name")
        self.assertEqual(self.config.site_description, "description")
        self.assertEqual(self.config.canonical_url, "https://www.site.com")
        self.assertEqual(self.config.publisher, "author")
        self.assertEqual(self.config.email, "my@email.org")
        self.assertEqual(self.config.favicon, "path/to/favicon.png")
        self.assertEqual(self.config.site_img, "pat/to/img.png")
        self.assertEqual(self.config.enable_ads, True)
        self.assertEqual(self.config.enable_analytics, True)


class HomeMsgModel(TestCase):
    def setUp(self):
        HomeMsg.objects.create(content="content")
        self.message = HomeMsg.objects.get()

    def test_home_msg_model_default(self):
        self.assertEqual(self.message.content, "content")
        self.assertEqual(self.message.enabled, False)

    def test_home_msg_model_modified(self):
        self.message.enabled = True
        self.message.save()
        self.assertEqual(self.message.enabled, True)
