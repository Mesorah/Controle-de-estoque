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

    def clean_barcode(self):
        barcode = self.cleaned_data['barcode']

        if len(barcode) != 13:
            self.add_error(
                'barcode', 'The size of barcode field has to be 13 digits'
            )

        return barcode

    def __init__(self, *args, **kwargs):
        super(CreateProductForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-verify'
