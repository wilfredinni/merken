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

    def test_CustomUser_model(self):
        user = CustomUser.objects.get(username="test_user")
        self.assertEqual(user.username, "test_user")
        self.assertEqual(user.email, "test_user@test_user.com")

    def test_CustomUser_model_custom_fields(self):
        user = CustomUser.objects.get(username="test_user")
        self.assertEqual(user.twitter, 'twitter')
        self.assertEqual(user.github, 'github')
        self.assertEqual(user.website, 'website')
        self.assertEqual(user.about, 'about')
