# Generated by Django 4.0.3 on 2022-03-07 15:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hospital', '0016_rename_underwriter_placement_exempt'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='placement',
            name='exempt',
        ),
        migrations.RemoveField(
            model_name='placement',
            name='patient',
        ),
        migrations.RemoveField(
            model_name='placement',
            name='services',
        ),
        migrations.DeleteModel(
            name='Patient',
        ),
        migrations.DeleteModel(
            name='Placement',
        ),
    ]
