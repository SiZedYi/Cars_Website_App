# Generated by Django 4.2.1 on 2023-06-21 07:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0005_alter_product_options_alter_product_deleted_at_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='product',
            options={'ordering': ('-modified_at',)},
        ),
    ]
