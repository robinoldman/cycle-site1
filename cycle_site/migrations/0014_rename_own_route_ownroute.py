# Generated by Django 3.2.19 on 2023-06-27 17:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cycle_site', '0013_remove_siteroutecomment_slug'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='own_route',
            new_name='OwnRoute',
        ),
    ]
