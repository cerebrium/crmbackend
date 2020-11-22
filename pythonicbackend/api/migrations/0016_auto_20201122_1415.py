# Generated by Django 3.0.8 on 2020-11-22 14:15

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0015_auto_20201112_2052'),
    ]

    operations = [
        migrations.CreateModel(
            name='RentalVanLock',
            fields=[
                ('rental_id', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('date', models.CharField(max_length=30, null=True)),
            ],
        ),
        migrations.AlterField(
            model_name='invoice',
            name='date',
            field=models.CharField(default=datetime.date(2020, 11, 22), max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='managers',
            name='creationDate',
            field=models.CharField(default=datetime.date(2020, 11, 22), max_length=50),
        ),
        migrations.AlterField(
            model_name='scheduleddate',
            name='date',
            field=models.CharField(default=datetime.date(2020, 11, 22), max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='vehiclescheduleddate',
            name='date',
            field=models.CharField(default=datetime.date(2020, 11, 22), max_length=50, null=True),
        ),
    ]
