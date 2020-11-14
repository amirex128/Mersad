# Generated by Django 3.1.3 on 2020-11-13 09:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Patrol',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('team_realm', models.CharField(max_length=500)),
                ('team_base', models.CharField(max_length=500)),
                ('charges', models.CharField(max_length=500)),
                ('leader', models.CharField(max_length=500)),
                ('responsibility_leader', models.CharField(max_length=500)),
                ('patrol_started_at', models.CharField(max_length=500)),
                ('serial_ruling', models.CharField(max_length=500)),
                ('ruling_started_at', models.CharField(max_length=500)),
                ('area', models.CharField(max_length=500)),
                ('realm', models.CharField(max_length=500)),
                ('teams', models.CharField(max_length=500)),
                ('time_started_at', models.CharField(max_length=500)),
                ('time_ended_at', models.CharField(max_length=500)),
                ('places', models.CharField(max_length=500)),
            ],
        ),
    ]