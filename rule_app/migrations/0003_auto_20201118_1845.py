# Generated by Django 3.1.3 on 2020-11-18 15:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rule_app', '0002_auto_20201114_1325'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rule',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
