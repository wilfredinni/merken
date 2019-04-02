from django.test import TestCase
from ..models import CustomUser


class CustomUserModel(TestCase):
    def setUp(self):
        CustomUser.objects.create_user(
            username="test_user",
            email="test_user@test_user.com",

            # custom fields
            twitter="twitter",
            github="github",
            website="website",
            about="about",
        )
        self.user = CustomUser.objects.get(username="test_user")

    def test_CustomUser_model(self):
        self.assertEqual(self.user.username, "test_user")
        self.assertEqual(self.user.email, "test_user@test_user.com")

    def test_CustomUser_model_custom_fields(self):
        self.assertEqual(self.user.twitter, "twitter")
        self.assertEqual(self.user.github, "github")
        self.assertEqual(self.user.website, "website")
        self.assertEqual(self.user.about, "about")
