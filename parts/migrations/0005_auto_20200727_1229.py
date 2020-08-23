# Generated by Django 3.0.6 on 2020-07-27 12:29

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('parts', '0004_sales_supply'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Person',
        ),
        migrations.AlterField(
            model_name='bike_models',
            name='entry_date',
            field=models.DateTimeField(default=django.utils.timezone.now, editable=False),
        ),
        migrations.AlterField(
            model_name='body_types',
            name='entry_date',
            field=models.DateTimeField(default=django.utils.timezone.now, editable=False),
        ),
        migrations.AlterField(
            model_name='brands',
            name='entry_date',
            field=models.DateTimeField(default=django.utils.timezone.now, editable=False),
        ),
        migrations.AlterField(
            model_name='parts_categories',
            name='entry_date',
            field=models.DateTimeField(default=django.utils.timezone.now, editable=False),
        ),
        migrations.AlterField(
            model_name='product',
            name='entry_date',
            field=models.DateTimeField(default=django.utils.timezone.now, editable=False),
        ),
        migrations.AlterField(
            model_name='sales',
            name='entry_date',
            field=models.DateTimeField(default=django.utils.timezone.now, editable=False),
        ),
        migrations.AlterField(
            model_name='store',
            name='entry_date',
            field=models.DateTimeField(default=django.utils.timezone.now, editable=False),
        ),
        migrations.AlterField(
            model_name='subcategories',
            name='entry_date',
            field=models.DateTimeField(default=django.utils.timezone.now, editable=False),
        ),
        migrations.AlterField(
            model_name='suppliers',
            name='entry_date',
            field=models.DateTimeField(default=django.utils.timezone.now, editable=False),
        ),
        migrations.AlterField(
            model_name='supplies',
            name='entry_date',
            field=models.DateTimeField(default=django.utils.timezone.now, editable=False),
        ),
    ]
