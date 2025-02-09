from django.contrib import admin

from product import models


@admin.register(models.Product)
class Product(admin.ModelAdmin):
    pass
