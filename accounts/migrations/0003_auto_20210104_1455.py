# Generated by Django 3.1.3 on 2021-01-04 12:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_auto_20201231_0702'),
    ]

    operations = [
        migrations.AlterField(
            model_name='useraccount',
            name='certificate',
            field=models.ImageField(blank=True, upload_to='certificates/%Y/%m/%d/', verbose_name='Сертификат'),
        ),
    ]
