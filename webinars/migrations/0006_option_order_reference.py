# Generated by Django 3.1.3 on 2021-02-25 16:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webinars', '0005_auto_20210225_1609'),
    ]

    operations = [
        migrations.AddField(
            model_name='option',
            name='order_reference',
            field=models.CharField(max_length=30, null=True, verbose_name='Уникальный номер заказа'),
        ),
    ]
