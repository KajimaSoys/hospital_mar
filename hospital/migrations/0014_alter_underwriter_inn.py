# Generated by Django 4.0.3 on 2022-03-07 14:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hospital', '0013_alter_underwriter_inn'),
    ]

    operations = [
        migrations.AlterField(
            model_name='underwriter',
            name='inn',
            field=models.CharField(max_length=10, verbose_name='ИНН страховой компании'),
        ),
    ]
