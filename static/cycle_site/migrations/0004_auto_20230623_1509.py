# Generated by Django 3.2.19 on 2023-06-23 15:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cycle_site', '0003_alter_own_route_slug'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='routecomment',
            name='email',
        ),
        migrations.RemoveField(
            model_name='routecomment',
            name='name',
        ),
    ]