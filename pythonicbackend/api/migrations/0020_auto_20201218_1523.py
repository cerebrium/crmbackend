# Generated by Django 3.0.8 on 2020-12-18 15:23

import datetime
from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0019_auto_20201211_1451'),
    ]

    operations = [
        migrations.CreateModel(
            name='DriverHistory',
            fields=[
                ('DriverHistory_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('date', models.CharField(max_length=30, null=True)),
                ('week_number', models.IntegerField(default=1, null=True, verbose_name='WEEKNUMBER')),
                ('driver_id', models.CharField(max_length=100, null=True)),
                ('registration', models.CharField(max_length=100, null=True)),
                ('name', models.CharField(max_length=30, null=True)),
            ],
        ),
        migrations.AlterField(
            model_name='invoice',
            name='date',
            field=models.CharField(default=datetime.date(2020, 12, 18), max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='managers',
            name='creationDate',
            field=models.CharField(default=datetime.date(2020, 12, 18), max_length=50),
        ),
        migrations.AlterField(
            model_name='scheduleddate',
            name='date',
            field=models.CharField(default=datetime.date(2020, 12, 18), max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='vehiclescheduleddate',
            name='date',
            field=models.CharField(default=datetime.date(2020, 12, 18), max_length=50, null=True),
        ),
    ]
