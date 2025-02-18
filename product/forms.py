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

# Criar verificação em js nesse form
