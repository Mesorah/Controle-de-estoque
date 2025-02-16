from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse


class TestHome(TestCase):
    def setUp(self):
        data = {
            'username': 'TestSuperUserUsername',
            'password': 'TestSuperUserPassword123'
        }

        User.objects.create_superuser(**data)

        self.client.login(**data)

        return super().setUp()

    def test_if_status_code_is_200_and_html_language_is_correct(self):
        response = self.client.get(reverse('product:home'))

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context['html_language'], 'en')
