# Generated by Django 4.1.2 on 2022-11-09 11:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='grado',
            name='duracion',
            field=models.IntegerField(default=4),
        ),
    ]