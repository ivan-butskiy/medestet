# Generated by Django 3.1.3 on 2020-12-22 20:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='old_price',
            field=models.PositiveIntegerField(blank=True, help_text='Больше, чем нынешняя', verbose_name='старая цена'),
        ),
    ]
