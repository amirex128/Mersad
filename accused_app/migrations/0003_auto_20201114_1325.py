# Generated by Django 3.1.3 on 2020-11-14 09:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accused_app', '0002_auto_20201113_1556'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='accused',
            table='accuseds',
        ),
        migrations.AlterModelTable(
            name='crime',
            table='crimes',
        ),
    ]
