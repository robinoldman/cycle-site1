# Generated by Django 3.2.19 on 2023-05-24 09:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cycle_site', '0008_auto_20230519_0942'),
    ]

    operations = [
        migrations.CreateModel(
            name='Event1',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='enter name', max_length=80)),
                ('start_time', models.TimeField()),
                ('end_time', models.TimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Event2',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='enter name', max_length=80)),
                ('start_time', models.TimeField()),
                ('end_time', models.TimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Event3',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='enter name', max_length=80)),
                ('start_time', models.TimeField()),
                ('end_time', models.TimeField()),
            ],
        ),
    ]
