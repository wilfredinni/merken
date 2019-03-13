from django.test import TestCase
from ..models import CustomUser


class CustomUserModel(TestCase):
    def setUp(self):
        CustomUser.objects.create_user(
            username='test_user',
            email='test_user@test_user.com',
        )

    def test_custom_user_model(self):
        user = CustomUser.objects.get(username='test_user')
        self.assertEqual(user.username, 'test_user')
        self.assertEqual(user.email, 'test_user@test_user.com')
