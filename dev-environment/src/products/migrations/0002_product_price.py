# Generated by Django 2.0.2 on 2018-02-15 13:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='price',
            field=models.DecimalField(decimal_places=2, default=0.99, max_digits=20),
        ),
    ]
