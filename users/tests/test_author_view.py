from django.test import TestCase
from django.urls import reverse, resolve

from users.models import CustomUser

from ..views import ProfileView


class AuthorTest(TestCase):
    def setUp(self):
        CustomUser.objects.create_user(username="test_user")

    def test_author_view_status_code(self):
        url = reverse("users_app:profile", kwargs={"slug": "test_user"})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_author_view_not_found_404(self):
        url = reverse("users_app:profile", kwargs={"slug": "wrong_user"})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 404)

    def test_url_resolves_author_view(self):
        view = resolve('/author/test_user')
        self.assertEqual(view.func.view_class, ProfileView)