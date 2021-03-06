# Generated by Django 2.0.6 on 2018-07-03 10:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vacancies', '0008_auto_20180630_0934'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vacancy',
            name='employment_type',
            field=models.CharField(choices=[('FT', 'Полный рабочий день'), ('PT', 'Не полный рабочий день'), ('TMP', 'Проект/временно'), ('VOL', 'Волонтерство'), ('INT', 'Стажировка')], default='FT', max_length=3),
        ),
        migrations.AlterField(
            model_name='vacancy',
            name='experience',
            field=models.CharField(choices=[('0', 'Без опыта'), ('1-3', '1-3 лет'), ('3-6', '3-6 лет'), ('6+', '6 лет и более')], default='0', max_length=3),
        ),
        migrations.AlterField(
            model_name='vacancy',
            name='status',
            field=models.IntegerField(choices=[(0, 'Не опубликовано'), (1, 'Опубликовано')], default=0),
        ),
        migrations.AlterField(
            model_name='vacancy',
            name='working_hours',
            field=models.CharField(choices=[('FT', 'Полный рабочий день'), ('FLT', 'Гибкий график'), ('RJ', 'Удаленная работа')], default='FLT', max_length=3),
        ),
    ]
