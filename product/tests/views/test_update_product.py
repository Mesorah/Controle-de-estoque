from django.test import TestCase
from django.urls import reverse

from utils.tests.product import create_session_product
from utils.tests.user import create_super_user


class TestUpdateProduct(TestCase):
    def setUp(self):
        username, password = create_super_user()
        self.client.login(username=username, password=password)

        self.data = create_session_product()
        self.client.post(reverse('product:create'), data=self.data)

        return super().setUp()

    def test_returns_status_code_302(self):
        response = self.client.post(
            reverse('product:delete', kwargs={'id': '1'})
        )

        self.assertEqual(response.status_code, 302)
