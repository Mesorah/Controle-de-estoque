from django.test import TestCase
from django.urls import reverse

from utils.tests.product import create_session_product
from utils.tests.user import create_super_user


class UpdateProductSession(TestCase):
    def setUp(self):
        username, password = create_super_user()
        self.client.login(username=username, password=password)

        self.data = create_session_product()
        self.client.post(reverse('product:create'), data=self.data)

        return super().setUp()

    def test_returns_status_code_200(self):
        response = self.client.get(reverse('product:update_session', kwargs={
            'id': '1'
        }))

        self.assertEqual(response.status_code, 200)

    def test_returns_status_code_302(self):
        self.data['stock'] = 2
        response = self.client.post(reverse('product:update_session', kwargs={
            'id': '1'
        }), data=self.data)

        self.assertEqual(response.status_code, 302)

    def test_if_form_except_typerror_error_404(self):
        response = self.client.get(reverse('product:update_session', kwargs={
            'id': '2'
        }))

        self.assertEqual(response.status_code, 302)

    def test_form_is_invalid(self):
        self.data['barcode'] = 123

        response = self.client.post(reverse('product:update_session', kwargs={
            'id': '1'
        }), data=self.data)

        self.assertEqual(response.status_code, 200)
