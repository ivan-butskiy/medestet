# Generated by Django 3.1.3 on 2021-02-26 11:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('videos', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='video',
            name='video',
            field=models.URLField(help_text='В формате "http://..."', verbose_name='ссылка на видео с YouTube'),
        ),
    ]