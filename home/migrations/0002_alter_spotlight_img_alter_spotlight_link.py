# Generated by Django 4.2.1 on 2023-05-24 12:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='spotlight',
            name='img',
            field=models.TextField(default=''),
        ),
        migrations.AlterField(
            model_name='spotlight',
            name='link',
            field=models.TextField(default=''),
        ),
    ]
