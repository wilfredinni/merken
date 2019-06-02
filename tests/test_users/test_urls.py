from django.test import TestCase
from django.urls import resolve, reverse

from apps.users.views import ProfileView


class AuthorTest(TestCase):
    def test_author_url_resolves(self):
        url = reverse("users_app:profile", args=["test_slug"])
        self.assertEqual(resolve(url).func.view_class, ProfileView)
