# Generated by Django 3.1.3 on 2020-11-13 09:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Accused',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=500, null=True)),
                ('last_name', models.CharField(max_length=500, null=True)),
                ('nation_code', models.IntegerField(null=True, unique=True)),
                ('image', models.ImageField(null=True, upload_to='')),
                ('birthday', models.DateField(null=True)),
                ('father_name', models.CharField(max_length=500, null=True)),
                ('birth_city', models.CharField(default='', max_length=500)),
                ('address', models.CharField(max_length=1000, null=True)),
                ('arrest_at', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Crime',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=500)),
                ('description', models.TextField(null=True)),
                ('address', models.CharField(max_length=1000, null=True)),
                ('accused', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accused_app.accused')),
            ],
        ),
    ]