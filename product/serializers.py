from rest_framework import serializers

from .models import Product


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = [
            'name', 'description', 'stock',
            'barcode', 'category', 'cost_price',
            'sale_price'
        ]
