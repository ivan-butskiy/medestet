# Generated by Django 3.1.3 on 2021-02-14 14:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webinars', '0003_auto_20201216_1709'),
    ]

    operations = [
        migrations.AddField(
            model_name='webinar',
            name='video',
            field=models.URLField(blank=True, help_text='В формате "http://..."', verbose_name='ссылка на видео трансляцию вебинара'),
        ),
        migrations.AddField(
            model_name='webinar',
            name='video_record',
            field=models.URLField(blank=True, help_text='В формате "http://..."', null=True, verbose_name='ссылка на запись вебинара'),
        ),
    ]
