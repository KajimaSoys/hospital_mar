# Generated by Django 4.0.3 on 2022-03-07 14:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hospital', '0014_alter_underwriter_inn'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient',
            name='year',
            field=models.CharField(max_length=4, verbose_name='Год рождения пациента'),
        ),
    ]