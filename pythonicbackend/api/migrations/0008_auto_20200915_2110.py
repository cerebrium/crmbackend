# Generated by Django 3.0.8 on 2020-09-15 21:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0007_auto_20200915_1441'),
    ]

    operations = [
        migrations.AddField(
            model_name='deductiontype',
            name='date',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='supporttype',
            name='date',
            field=models.CharField(max_length=30, null=True),
        ),
    ]
