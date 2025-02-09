from django.test import TestCase

from product.models import Category


class TestCategory(TestCase):
    def test_if_category_name_is_correct(self):
        category = Category.objects.create(
            name='Fruits'
        )

        self.assertEqual(str(category), 'Fruits')
