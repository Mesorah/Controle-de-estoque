from rest_framework import serializers
from rest_framework.validators import ValidationError

from product.validators import ProductValidator

from .models import Product


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = [
            'id', 'name', 'description',
            'stock', 'barcode', 'category',
            'cost_price', 'sale_price'
        ]

    def validate(self, attrs):
        if self.instance is not None and attrs.get('description') is None:
            attrs['description'] = self.instance.description

        if self.instance is not None and attrs.get('barcode') is None:
            attrs['barcode'] = self.instance.barcode

        if self.instance is not None and attrs.get('cost_price') is None:
            attrs['cost_price'] = self.instance.cost_price

        if self.instance is not None and attrs.get('sale_price') is None:
            attrs['sale_price'] = self.instance.sale_price

        ProductValidator(
            data=attrs,
            ErrorClass=ValidationError
        )

        return attrs
