from django.test import TestCase

from product.models import Category, Product


class TestProduct(TestCase):
    def test_if_product_name_is_correct(self):
        category = Category.objects.create(name='Fruit')

        kwargs = {
            'name': 'Manga',
            'description': 'The manga',
            'stock': 10,
            'barcode': '4535345343',
            'category': category
        }

        product = Product.objects.create(**kwargs)

        self.assertEqual(str(product), 'Manga')
