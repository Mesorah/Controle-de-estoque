from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response

from product.models import Product
from product.serializers import ProductSerializer


@api_view(['GET'])
def product_list(request):
    product = Product.objects.all()

    if request.method == 'GET':
        serializer = ProductSerializer(
            instance=product,
            many=True
        )

        return Response(serializer.data)


@api_view(['GET'])
def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)

    if request.method == 'GET':
        serializer = ProductSerializer(
            instance=product,
        )

        return Response(serializer.data)
