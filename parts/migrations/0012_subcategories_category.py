# Generated by Django 3.1 on 2020-10-21 06:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('parts', '0011_sales_profit'),
    ]

    operations = [
        migrations.AddField(
            model_name='subcategories',
            name='category',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='parts.parts_categories'),
            preserve_default=False,
        ),
    ]
