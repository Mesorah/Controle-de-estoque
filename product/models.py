from django.db import models


class Product(models.Model):
    class Meta:
        verbose_name = 'Produto'
        verbose_name_plural = 'Produtos'

    name = models.CharField(max_length=255)
    description = models.TextField()
    stock = models.PositiveIntegerField()
    barcode = models.PositiveIntegerField()
