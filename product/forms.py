from django import forms

from product import models


class CreateProductForm(forms.ModelForm):
    class Meta:
        model = models.Product

        fields = [
            'name',
            'description',
            'stock',
            'barcode',
            'category',
            'cost_price',
            'sale_price'
        ]

    def clean_description(self):
        description = self.cleaned_data['description']

        if len(description) == 0:
            self.add_error('description', 'Incomplete field')

    def clean_barcode(self):
        barcode = self.cleaned_data['barcode']

        if len(barcode) != 13:
            self.add_error(
                'barcode', 'The size of barcode field has to be 13 digits'
            )

        return barcode

    def clean_cost_price(self):
        cost_price = self.cleaned_data['cost_price']

        if cost_price <= 0:
            self.add_error(
                'cost_price',
                'The cost price cannot be less than or equal to zero'
            )

        return cost_price

    def clean_sale_price(self):
        cost_price = self.cleaned_data['cost_price']
        sale_price = self.cleaned_data['sale_price']

        if cost_price > sale_price or cost_price == sale_price:
            self.add_error(
                'cost_price',
                ('The cost price cannot be greater than or equal'
                 'to the selling price')
            )

        return sale_price

    def __init__(self, *args, **kwargs):
        super(CreateProductForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-verify'
