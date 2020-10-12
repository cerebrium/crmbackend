# Generated by Django 3.0.8 on 2020-10-11 17:22

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0009_auto_20201002_1438'),
    ]

    operations = [
        migrations.AddField(
            model_name='scheduleddate',
            name='week_number',
            field=models.IntegerField(default=1, null=True, verbose_name='WEEKNUMBER'),
        ),
        migrations.AlterField(
            model_name='invoice',
            name='date',
            field=models.CharField(default=datetime.date(2020, 10, 11), max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='managers',
            name='creationDate',
            field=models.CharField(default=datetime.date(2020, 10, 11), max_length=50),
        ),
        migrations.AlterField(
            model_name='scheduleddate',
            name='date',
            field=models.CharField(default=datetime.date(2020, 10, 11), max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='vehiclescheduleddate',
            name='date',
            field=models.CharField(default=datetime.date(2020, 10, 11), max_length=50, null=True),
        ),
    ]
