# Generated by Django 3.1.3 on 2020-11-18 15:19

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('report_app', '0004_auto_20201118_1848'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patrol',
            name='time_ended_at',
            field=models.TimeField(default=datetime.datetime(2020, 11, 19, 3, 19, 47, 92978, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='patrol',
            name='time_started_at',
            field=models.TimeField(auto_now_add=True, null=True),
        ),
    ]
