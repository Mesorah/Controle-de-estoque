from django.test import TestCase
from django.urls import reverse

from utils.tests.user import create_super_user


class TestLogin(TestCase):
    def setUp(self):
        username, password = create_super_user()

        self.client.login(username=username, password=password)

        return super().setUp()

    def test_if_user_login_post_status_code_is_302(self):
        response = self.client.post(reverse('authors:login'), data={
            'username': 'usernameTest',
            'password': 'passwordTest123'
        })

        self.assertEqual(response.status_code, 302)
