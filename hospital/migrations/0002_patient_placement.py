# Generated by Django 4.0.3 on 2022-03-02 17:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hospital', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='patient',
            name='placement',
            field=models.ManyToManyField(to='hospital.placement', verbose_name='Посещение стационара'),
        ),
    ]
