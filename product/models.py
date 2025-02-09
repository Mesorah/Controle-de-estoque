from django.db import models


class Category(models.Model):
    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'

    category = models.CharField(max_length=255)


class Product(models.Model):
    class Meta:
        verbose_name = 'Produto'
        verbose_name_plural = 'Produtos'

    name = models.CharField(max_length=255)
    description = models.TextField()
    stock = models.PositiveIntegerField()
    barcode = models.PositiveIntegerField()
    category = models.ForeignKey(
        Category, on_delete=models.SET_NULL, null=True
    )
