# Generated by Django 3.2.19 on 2023-05-19 09:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cycle_site', '0007_auto_20230519_0940'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='end_time',
            field=models.TimeField(),
        ),
        migrations.AlterField(
            model_name='event',
            name='start_time',
            field=models.TimeField(),
        ),
    ]