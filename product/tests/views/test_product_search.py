from django.test import TestCase
from django.urls import reverse

from product.models import Product
from utils.tests.user import create_super_user


class TestProductSearch(TestCase):
    def setUp(self):
        username, password = create_super_user()

        self.client.login(username=username, password=password)

        product_data = {
            'name': 'TestProductName',
            'stock': 10,
            'cost_price': 15.99,
            'sale_price': 20.99,
        }

        Product.objects.create(**product_data)

        return super().setUp()

    def test_if_search_is_correct(self):
        response = self.client.get(
            reverse('product:search') + '?search=TestProductName'
        )

        self.assertIn(
            'Product Name: TestProductName', response.content.decode('-utf8')
        )
