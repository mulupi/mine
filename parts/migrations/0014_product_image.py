# Generated by Django 3.1 on 2020-10-21 06:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('parts', '0013_remove_subcategories_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='image',
            field=models.ImageField(default=1, upload_to='images/products/'),
            preserve_default=False,
        ),
    ]
