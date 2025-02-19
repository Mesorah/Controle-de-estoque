from django.db import models


class Category(models.Model):
    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'

    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Product(models.Model):
    class Meta:
        verbose_name = 'Produto'
        verbose_name_plural = 'Produtos'

    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    stock = models.PositiveIntegerField()
    barcode = models.CharField(max_length=13)
    category = models.ForeignKey(
        Category, on_delete=models.SET_NULL, null=True)
    cost_price = models.FloatField(null=True, default=0)
    sale_price = models.FloatField(null=True, default=0)

    def __str__(self):
        return self.name
