# Generated by Django 3.2.19 on 2023-05-17 11:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cycle_site', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='name',
            field=models.CharField(default='Default Name', max_length=80),
        ),
    ]