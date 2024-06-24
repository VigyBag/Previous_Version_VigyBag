# Generated by Django 4.1.6 on 2023-08-09 11:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Product', '0002_color_size_rename_price_product_sellingprice_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='info',
            field=models.CharField(default=1, max_length=2000),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='product',
            name='seller',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
    ]
