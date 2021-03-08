# Generated by Django 3.1.3 on 2021-02-21 11:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0007_auto_20210219_0330'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='course',
            options={'ordering': ['-pk'], 'verbose_name': 'курс', 'verbose_name_plural': 'курсы'},
        ),
        migrations.AlterModelOptions(
            name='courseorder',
            options={'ordering': ['-payment_date'], 'verbose_name': 'заказ курса', 'verbose_name_plural': 'заказы курсов'},
        ),
        migrations.AlterModelOptions(
            name='coursepromocode',
            options={'ordering': ['-pk'], 'verbose_name': 'промокод', 'verbose_name_plural': 'промокоды'},
        ),
        migrations.AlterModelOptions(
            name='lesson',
            options={'ordering': ['pk'], 'verbose_name': 'урок', 'verbose_name_plural': 'уроки'},
        ),
        migrations.AlterModelOptions(
            name='module',
            options={'ordering': ['pk'], 'verbose_name': 'модуль', 'verbose_name_plural': 'модули'},
        ),
        migrations.AlterModelOptions(
            name='person',
            options={'verbose_name': 'персонаж ЦА', 'verbose_name_plural': 'персонажи ЦА'},
        ),
        migrations.AlterModelOptions(
            name='subject',
            options={'verbose_name': 'субъект', 'verbose_name_plural': 'субъекты'},
        ),
        migrations.RemoveField(
            model_name='lesson',
            name='is_published',
        ),
        migrations.RemoveField(
            model_name='module',
            name='is_published',
        ),
    ]
