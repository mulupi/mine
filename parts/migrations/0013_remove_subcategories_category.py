# Generated by Django 3.1 on 2020-10-21 06:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('parts', '0012_subcategories_category'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='subcategories',
            name='category',
        ),
    ]
