from django.test import TestCase
from django.urls import reverse

from product.models import Category
from utils.tests.user import create_super_user


class TestCreateProduct(TestCase):
    def setUp(self):
        username, password = create_super_user()
        self.client.login(username=username, password=password)

        category = Category.objects.create(name='TestCategory')

        self.data = {
            'name': 'TestProduct',
            'description': 'TestDescription',
            'stock': 10,
            'barcode': '1111111111111',
            'category': category.id,
            'cost_price': 5.99,
            'sale_price': 7.99
        }

        return super().setUp()

    def test_returns_status_code_200(self):
        response = self.client.get(reverse('product:create'))

        self.assertEqual(response.status_code, 200)

    def test_returns_status_code_302(self):
        response = self.client.post(reverse('product:create'), data=self.data)

        self.assertEqual(response.status_code, 302)

    def test_form_is_invalid(self):
        self.data['barcode'] = 123

        response = self.client.post(reverse('product:create'), data=self.data)

        self.assertEqual(response.status_code, 200)

    def test_products_stored_separately_in_session(self):
        self.client.post(reverse('product:create'), data=self.data)

        self.data['name'] = 'TestProduct2'
        self.client.post(reverse('product:create'), data=self.data)
        session = self.client.session

        self.assertNotEqual(session['products']['1'], session['products']['2'])
