from django import forms
from django.forms import ValidationError

from product import models

from .validators import ProductValidator


class CreateProductForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(CreateProductForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-verify'

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

    def clean(self):
        cleaned_data = super().clean()

        ProductValidator(
            data=cleaned_data,
            ErrorClass=ValidationError
        )

        return cleaned_data
