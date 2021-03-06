# Generated by Django 3.1.3 on 2020-12-15 17:44

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Workshop',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField(help_text='Поле автозаполняемо. Должно быть уникально.', unique=True, verbose_name='слаг')),
                ('title', models.CharField(help_text='Название семинара. Служит заголовком на лендинге. Если семинары по этой теме уже проводились, желательно, чтобы было в едином стиле с предыдущими. Макс. длина 200 символов.', max_length=200, verbose_name='название семинара')),
                ('subtitle', models.CharField(help_text='Макс. длина 250 символов.', max_length=250, verbose_name='подзаголовок')),
                ('header_image', models.ImageField(help_text='Главное изображение, которое выводится в шапке лендинга.', upload_to='workshops/%Y-%m-%d/', verbose_name='главное изображение')),
                ('starting_date', models.DateField(help_text='Дата начала семинара', verbose_name='дата начала')),
                ('description', models.TextField(verbose_name='описание семинара')),
                ('description_image', models.ImageField(upload_to='workshops/%Y-%m-%d/', verbose_name='картинка к описанию')),
                ('location', models.CharField(help_text='Адрес места проведения. Макс. длина 200 символов.', max_length=200, verbose_name='место проведения')),
                ('location_image', models.ImageField(help_text='Скрин с гугл карты места проведения семинара или фото заведения.', upload_to='workshops/%Y-%m-%d/', verbose_name='изображение локации')),
                ('adding_date', models.DateTimeField(auto_now_add=True, verbose_name='дата добавления')),
                ('is_published', models.BooleanField(default=True, verbose_name='опубликован на сайте')),
                ('is_started', models.BooleanField(default=False, help_text='Если начат, желательно снять галочку с "Опубликован на сайте", чтобы во время его проведения семинар не показывался на сайте, а люди не могли записаться.', verbose_name='семинар начат')),
                ('students', models.ManyToManyField(blank=True, to=settings.AUTH_USER_MODEL, verbose_name='участники семинара')),
            ],
            options={
                'verbose_name': 'семинар',
                'verbose_name_plural': 'семинары',
                'ordering': ['starting_date'],
            },
        ),
        migrations.CreateModel(
            name='Option',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(help_text='Развание варианта участия. Макс. длина 150 символов.', max_length=150, verbose_name='название')),
                ('description', models.CharField(help_text='Макс. длина 300 символов.', max_length=300, verbose_name='описание варианта участия')),
                ('price', models.DecimalField(decimal_places=0, help_text='Введите целое число без дробной части.', max_digits=5, verbose_name='стоимость варианта участия')),
                ('workshop', models.ForeignKey(help_text='К какому семинару относится.', on_delete=django.db.models.deletion.CASCADE, to='workshops.workshop', verbose_name='семинар')),
            ],
        ),
        migrations.CreateModel(
            name='Lesson',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(help_text='Макс. длина 150 символов.', max_length=150, verbose_name='название занятия')),
                ('short_description', models.CharField(help_text='Макс. длина 200 символов.', max_length=200, verbose_name='краткое описание занятия')),
                ('starting_date', models.DateTimeField(verbose_name='время и дата начала занятия')),
                ('is_published', models.BooleanField(default=True, help_text='Занятие показано на лендинге семинара и в кабинете пользователя.', verbose_name='опубликовано')),
                ('is_active', models.BooleanField(default=False, verbose_name='занятие началось')),
                ('workshop', models.ForeignKey(help_text='К какому семинару относится занятие.', on_delete=django.db.models.deletion.CASCADE, to='workshops.workshop', verbose_name='семинар')),
            ],
            options={
                'verbose_name': 'занятие',
                'verbose_name_plural': 'занятия',
                'ordering': ['starting_date'],
            },
        ),
    ]
