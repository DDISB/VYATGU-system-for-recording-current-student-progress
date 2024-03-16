# Generated by Django 5.0.1 on 2024-03-16 12:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ElectronicJournal', '0009_teacher_user'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='active',
            options={'verbose_name': 'Событие', 'verbose_name_plural': 'События'},
        ),
        migrations.AlterModelOptions(
            name='groupa',
            options={'verbose_name': 'Группы', 'verbose_name_plural': 'Группы'},
        ),
        migrations.AlterModelOptions(
            name='pair',
            options={'verbose_name': 'Пары', 'verbose_name_plural': 'Пары'},
        ),
        migrations.AlterModelOptions(
            name='pairactive',
            options={'verbose_name': 'Активность на паре', 'verbose_name_plural': 'Активность на паре'},
        ),
        migrations.AlterModelOptions(
            name='student',
            options={'verbose_name': 'Студент', 'verbose_name_plural': 'Студенты'},
        ),
        migrations.AlterModelOptions(
            name='subject',
            options={'verbose_name': 'Предмет', 'verbose_name_plural': 'Предметы'},
        ),
        migrations.AlterModelOptions(
            name='teacher',
            options={'verbose_name': 'Преподаватель', 'verbose_name_plural': 'Преподаватели'},
        ),
        migrations.AlterModelOptions(
            name='typeactive',
            options={'verbose_name': 'Тип события', 'verbose_name_plural': 'Тип события'},
        ),
        migrations.AlterModelOptions(
            name='typesubject',
            options={'verbose_name': 'Тип предмета', 'verbose_name_plural': 'Тип предмета'},
        ),
    ]
