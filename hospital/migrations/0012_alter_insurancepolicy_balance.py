# Generated by Django 4.0.3 on 2022-03-07 12:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hospital', '0011_alter_underwriter_comp_address'),
    ]

    operations = [
        migrations.AlterField(
            model_name='insurancepolicy',
            name='balance',
            field=models.BigIntegerField(default=15000, verbose_name='Баланс страхового полиса'),
        ),
    ]