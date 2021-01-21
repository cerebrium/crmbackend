# Generated by Django 3.0.8 on 2021-01-20 16:22

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0025_auto_20210118_2012'),
    ]

    operations = [
        migrations.AddField(
            model_name='dailymessage',
            name='name',
            field=models.CharField(max_length=300, null=True),
        ),
        migrations.AddField(
            model_name='dailymessage',
            name='station',
            field=models.CharField(default='DBS2', max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name='dailymessage',
            name='message',
            field=models.CharField(max_length=900, null=True),
        ),
        migrations.AlterField(
            model_name='invoice',
            name='date',
            field=models.CharField(default=datetime.date(2021, 1, 20), max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='managers',
            name='creationDate',
            field=models.CharField(default=datetime.date(2021, 1, 20), max_length=50),
        ),
        migrations.AlterField(
            model_name='scheduleddate',
            name='date',
            field=models.CharField(default=datetime.date(2021, 1, 20), max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='vehiclescheduleddate',
            name='date',
            field=models.CharField(default=datetime.date(2021, 1, 20), max_length=50, null=True),
        ),
    ]
