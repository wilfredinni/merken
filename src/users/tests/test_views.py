from django.test import TestCase, Client
from django.urls import reverse

from users.models import CustomUser


class TestAuthor(TestCase):
    def setUp(self):
        self.client = Client()
        CustomUser.objects.create_user(username="test_user")

    def test_author_GET(self):
        url = reverse("users_app:profile", args=["test_user"])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "users/author.html")

    def test_author_view_not_found_404(self):
        url = reverse("users_app:profile", args=["wrong_user"])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 404)
