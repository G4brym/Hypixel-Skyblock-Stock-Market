# Generated by Django 3.0.7 on 2020-06-10 09:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_product_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='slug',
            field=models.SlugField(blank=True, editable=False, max_length=128, null=True),
        ),
    ]
