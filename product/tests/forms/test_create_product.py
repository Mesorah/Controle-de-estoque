from django.test import TestCase

from product.forms import CreateProductForm


class TestCreateProduct(TestCase):
    def test_if_description_length_is_zero(self):
        form_data = {'description': ''}
        form = CreateProductForm(data=form_data)
        self.assertIn('Incomplete field', form.errors['description'])

    def test_description_length_is_greater_than_zero(self):
        form_data = {'description': 'Hello'}
        form = CreateProductForm(data=form_data)
        self.assertNotIn('description', form.errors)

    def test_if_barcode_length_is_less_than_thirteen(self):
        form_data = {'barcode': '1234567890'}
        form = CreateProductForm(data=form_data)
        self.assertIn(
            'The size of barcode field has to be 13 digits',
            form.errors['barcode']
        )

    def test_if_barcode_length_is_thirteen(self):
        form_data = {'barcode': '1234567890123'}
        form = CreateProductForm(data=form_data)
        self.assertNotIn('barcode', form.errors)

    def test_cost_price_is_zero_or_negative(self):
        form_data = {'cost_price': 0}
        form = CreateProductForm(data=form_data)
        self.assertIn(
            'The cost price cannot be less than or equal to zero',
            form.errors['cost_price']
        )

        form_data = {'cost_price': -1}
        form = CreateProductForm(data=form_data)
        self.assertIn(
            'The cost price cannot be less than or equal to zero',
            form.errors['cost_price']
        )

    def test_cost_price_is_not_zero_or_negative(self):
        form_data = {'cost_price': 1}
        form = CreateProductForm(data=form_data)
        self.assertNotIn('cost_price', form.errors)

    def test_cost_price_greater_than_selling_price(self):
        form_data = {'cost_price': 5, 'sale_price': 5}
        form = CreateProductForm(data=form_data)
        self.assertIn(
            ('The cost price cannot be greater than or equal'
             'to the selling price'), form.errors['cost_price']
        )

        form_data = {'cost_price': 5, 'sale_price': 4}
        form = CreateProductForm(data=form_data)
        self.assertIn(
            ('The cost price cannot be greater than or equal'
             'to the selling price'), form.errors['cost_price']
        )

    def test_cost_price_less_than_selling_price(self):
        form_data = {'cost_price': 4, 'sale_price': 5}
        form = CreateProductForm(data=form_data)
        self.assertNotIn('cost_price', form.errors)
