from django.test import TestCase
from django.urls import reverse

from utils.tests.user import create_super_user


class TestHome(TestCase):
    def setUp(self):
        username, password = create_super_user()

        self.client.login(username=username, password=password)

        return super().setUp()

    def test_if_status_code_is_200_and_html_language_is_correct(self):
        response = self.client.get(reverse('product:home'))

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context['html_language'], 'en')
