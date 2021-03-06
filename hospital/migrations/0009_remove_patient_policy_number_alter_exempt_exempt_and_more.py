# Generated by Django 4.0.3 on 2022-03-07 11:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hospital', '0008_rename_exempt_tнpe_exempt_exempt_type'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='patient',
            name='policy_number',
        ),
        migrations.AlterField(
            model_name='exempt',
            name='exempt',
            field=models.PositiveIntegerField(default=0, verbose_name='Сумма льготы(%)'),
        ),
        migrations.CreateModel(
            name='InsurancePolicy',
            fields=[
                ('id', models.BigAutoField(default=1160000000, primary_key=True, serialize=False, verbose_name='ИД полиса')),
                ('balance', models.IntegerField(default=15000, verbose_name='Баланс страхового полиса')),
                ('underwriter', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hospital.underwriter', verbose_name='Страхования компания')),
            ],
            options={
                'verbose_name': 'Страховой полис',
                'verbose_name_plural': 'Страховые полисы',
            },
        ),
    ]
