# Generated by Django 4.0.3 on 2022-03-09 20:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hospital', '0022_alter_patient_policy_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='placement',
            name='exempt',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='hospital.exempt', verbose_name='Льгота'),
        ),
    ]
