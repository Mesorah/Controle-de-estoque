from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from product.models import Product
from product.serializers import ProductSerializer


@api_view(['GET', 'POST'])
def product_list(request):
    product = Product.objects.all()

    if request.method == 'GET':
        serializer = ProductSerializer(
            instance=product,
            many=True
        )

        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = ProductSerializer(data=request.data)

        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(
            serializer.data,
            status=status.HTTP_201_CREATED
        )


@api_view(['GET', 'PATCH', 'DELETE'])
def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)

    if request.method == 'GET':
        serializer = ProductSerializer(instance=product)

        return Response(serializer.data)

    elif request.method == 'PATCH':
        serializer = ProductSerializer(
            instance=product,
            data=request.data,
            partial=True
        )

        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(
            serializer.data,
            status=status.HTTP_200_OK
        )

    elif request.method == 'DELETE':
        product.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)
