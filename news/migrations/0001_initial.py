# Generated by Django 3.1.3 on 2021-02-26 03:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField(help_text='Поле автозаполняемо. Должно быть уникально', unique=True, verbose_name='Слаг')),
                ('title', models.CharField(max_length=200, verbose_name='название новости. Макс. длина 200 символов')),
                ('subtitle', models.CharField(blank=True, help_text='Не обязательно к заполнению', max_length=300, verbose_name='подзаголовок. Макс. длина 300 символов')),
                ('image', models.ImageField(help_text='Главное изображение, которое выводится в миниатюре и шапке лендинга', upload_to='news/%Y-%m-%d/', verbose_name='изображение')),
                ('text', models.TextField(verbose_name='текст новости')),
                ('adding_date', models.DateTimeField(auto_now_add=True, verbose_name='дата добавления новости')),
                ('update_date', models.DateTimeField(auto_now=True, verbose_name='дата обновления новости')),
                ('is_published', models.BooleanField(default=True, verbose_name='Опубликовано и показано на сайте')),
            ],
            options={
                'verbose_name': 'новость',
                'verbose_name_plural': 'новости',
                'ordering': ['-update_date', '-adding_date'],
            },
        ),
    ]
