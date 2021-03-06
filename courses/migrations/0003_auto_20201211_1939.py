# Generated by Django 3.1.3 on 2020-12-11 17:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0002_auto_20201211_1759'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lesson',
            name='module',
            field=models.ForeignKey(help_text='К какому модулю относится урок.', on_delete=django.db.models.deletion.CASCADE, to='courses.module', verbose_name='модуль'),
        ),
        migrations.AlterField(
            model_name='person',
            name='course',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='courses.course', verbose_name='курс'),
        ),
    ]
