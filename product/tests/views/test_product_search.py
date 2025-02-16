from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse

from product.models import Product


class TestProductSearch(TestCase):
    def setUp(self):
        data = {
            'username': 'TestSuperUserUsername',
            'password': 'TestSuperUserPassword123'
        }

        User.objects.create_superuser(**data)

        self.client.login(**data)

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
