# Generated by Django 3.1 on 2020-10-21 06:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('parts', '0009_auto_20200923_0912'),
    ]

    operations = [
        migrations.AddField(
            model_name='supplies',
            name='price_per_unit',
            field=models.FloatField(default=10),
            preserve_default=False,
        ),
    ]
