# Generated by Django 4.2.1 on 2023-05-24 12:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_alter_brand_logo_alter_product_imgs_alter_type_img'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='sku',
        ),
        migrations.AddField(
            model_name='product',
            name='slug',
            field=models.SlugField(default='', unique=True),
        ),
    ]
