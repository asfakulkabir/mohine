# Generated by Django 4.2.4 on 2023-09-18 06:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mohine_products', '0002_alter_products_product_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='product_ammount',
            field=models.CharField(max_length=30),
        ),
    ]
