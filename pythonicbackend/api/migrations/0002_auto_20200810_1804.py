# Generated by Django 3.0.8 on 2020-08-10 18:04

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='managers',
            name='station',
        ),
        migrations.AddField(
            model_name='managers',
            name='DBS2',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='managers',
            name='DEX2',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='managers',
            name='DSN1',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='managers',
            name='DXP1',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='invoice',
            name='date',
            field=models.CharField(default=datetime.date(2020, 8, 10), max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='managers',
            name='creationDate',
            field=models.CharField(default=datetime.date(2020, 8, 10), max_length=50),
        ),
        migrations.AlterField(
            model_name='scheduleddate',
            name='date',
            field=models.CharField(default=datetime.date(2020, 8, 10), max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='vehiclescheduleddate',
            name='date',
            field=models.CharField(default=datetime.date(2020, 8, 10), max_length=50, null=True),
        ),
    ]