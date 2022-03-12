# Generated by Django 4.0.3 on 2022-03-03 07:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hospital', '0003_remove_patient_placement_placement_patient'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='exempt',
            options={'verbose_name': 'Льготы', 'verbose_name_plural': 'Льготы'},
        ),
        migrations.AlterModelOptions(
            name='patient',
            options={'verbose_name': 'Пациент', 'verbose_name_plural': 'Пациенты'},
        ),
        migrations.AlterModelOptions(
            name='placement',
            options={'verbose_name': 'Посещение стационара', 'verbose_name_plural': 'Посещения стационаров'},
        ),
        migrations.AlterModelOptions(
            name='service',
            options={'verbose_name': 'Услуга', 'verbose_name_plural': 'Услуги'},
        ),
        migrations.AlterModelOptions(
            name='specialization',
            options={'verbose_name': 'Специализация', 'verbose_name_plural': 'Специализации'},
        ),
        migrations.AlterModelOptions(
            name='staff',
            options={'verbose_name': 'Доктор', 'verbose_name_plural': 'Доктора'},
        ),
        migrations.AlterModelOptions(
            name='underwriter',
            options={'verbose_name': 'Страховая компания', 'verbose_name_plural': 'Страховая компании'},
        ),
        migrations.AlterModelOptions(
            name='university',
            options={'verbose_name': 'Университет', 'verbose_name_plural': 'Университеты'},
        ),
        migrations.RemoveField(
            model_name='staff',
            name='ext_staff',
        ),
        migrations.DeleteModel(
            name='ExtStaff',
        ),
    ]