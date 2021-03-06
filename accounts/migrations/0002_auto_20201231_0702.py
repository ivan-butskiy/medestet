# Generated by Django 3.1.3 on 2020-12-31 05:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='useraccount',
            name='buy_count',
            field=models.PositiveIntegerField(default=0, verbose_name='Количество покупок'),
        ),
        migrations.AddField(
            model_name='useraccount',
            name='buy_sum',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=8, verbose_name='Сумма покупок'),
        ),
        migrations.AlterField(
            model_name='useraccount',
            name='email',
            field=models.EmailField(db_index=True, max_length=50, unique=True, verbose_name='E-mail'),
        ),
        migrations.AlterField(
            model_name='useraccount',
            name='first_name',
            field=models.CharField(max_length=20, verbose_name='Имя'),
        ),
        migrations.AlterField(
            model_name='useraccount',
            name='is_active',
            field=models.BooleanField(default=True, verbose_name='Аккаунт активен'),
        ),
        migrations.AlterField(
            model_name='useraccount',
            name='is_certified',
            field=models.BooleanField(default=False, verbose_name='Сертифицирован'),
        ),
        migrations.AlterField(
            model_name='useraccount',
            name='is_staff',
            field=models.BooleanField(default=False, verbose_name='Сотрудник'),
        ),
        migrations.AlterField(
            model_name='useraccount',
            name='last_name',
            field=models.CharField(blank=True, max_length=20, verbose_name='Фамилия'),
        ),
        migrations.AlterField(
            model_name='useraccount',
            name='patronym',
            field=models.CharField(blank=True, max_length=20, verbose_name='Отчество'),
        ),
        migrations.AlterField(
            model_name='useraccount',
            name='phone',
            field=models.CharField(blank=True, max_length=20, verbose_name='Телефон'),
        ),
        migrations.AlterField(
            model_name='useraccount',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='photos/%Y-%m-%d/', verbose_name='Фото'),
        ),
        migrations.AlterField(
            model_name='useraccount',
            name='register_date',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Дата регистрации'),
        ),
    ]
