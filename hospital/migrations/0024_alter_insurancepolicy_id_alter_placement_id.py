# Generated by Django 4.0.3 on 2022-03-16 19:36

from django.db import migrations, models
import hospital.models


class Migration(migrations.Migration):

    dependencies = [
        ('hospital', '0023_alter_placement_exempt'),
    ]

    operations = [
        migrations.AlterField(
            model_name='insurancepolicy',
            name='id',
            field=models.BigIntegerField(default=hospital.models.default_insurance_id, primary_key=True, serialize=False, verbose_name='ИД полиса'),
        ),
        migrations.AlterField(
            model_name='placement',
            name='id',
            field=models.BigAutoField(default=hospital.models.default_id, primary_key=True, serialize=False, verbose_name='Идентификатор посещения'),
        ),
    ]