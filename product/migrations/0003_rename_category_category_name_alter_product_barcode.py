# Generated by Django 5.1.6 on 2025-02-09 19:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0002_category_product_category'),
    ]

    operations = [
        migrations.RenameField(
            model_name='category',
            old_name='category',
            new_name='name',
        ),
        migrations.AlterField(
            model_name='product',
            name='barcode',
            field=models.CharField(max_length=255),
        ),
    ]
