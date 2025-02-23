from django.test import TestCase
from django.urls import reverse

from utils.tests.product import create_session_product
from utils.tests.user import create_super_user


class TestDashboard(TestCase):
    def setUp(self):
        username, password = create_super_user()

        self.client.login(username=username, password=password)

        return super().setUp()

    def test_redirect_if_no_have_product_session(self):
        response = self.client.get(reverse('product:dashboard'))

        self.assertEqual(response.status_code, 302)

    def test_returns_correct_template(self):
        data = create_session_product()
        self.client.post(reverse('product:create'), data=data)

        response = self.client.get(reverse('product:dashboard'))

        self.assertTemplateUsed(response, 'product/dashboard.html')

    def test_returns_status_code_302(self):
        data = create_session_product()
        self.client.post(reverse('product:create'), data=data)

        response = self.client.post(reverse('product:dashboard'))

        self.assertEqual(response.status_code, 302)
