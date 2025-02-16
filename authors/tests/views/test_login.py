from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse


class TestLogin(TestCase):
    def setUp(self):
        User.objects.create_user(
            username='usernameTest',
            password='passwordTest123'
        )

        return super().setUp()

    def test_if_user_login_post_status_code_is_302(self):
        response = self.client.post(reverse('authors:login'), data={
            'username': 'usernameTest',
            'password': 'passwordTest123'
        })

        self.assertEqual(response.status_code, 302)
