from rest_framework.generics import (  # noqa E501
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView,
)
from rest_framework.pagination import PageNumberPagination

from product.models import Product
from product.serializers import ProductSerializer


class ProductAPIPagination(PageNumberPagination):
    page_size = 5


class ProductListAPIView(ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    pagination_class = ProductAPIPagination


class ProductDetailAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
