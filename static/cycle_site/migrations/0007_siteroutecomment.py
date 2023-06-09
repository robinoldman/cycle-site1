# Generated by Django 3.2.19 on 2023-06-25 08:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cycle_site', '0006_remove_routecomment_email'),
    ]

    operations = [
        migrations.CreateModel(
            name='SiteRouteComment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=80)),
                ('body', models.TextField()),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('approved', models.BooleanField(default=False)),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='route_comments', to='cycle_site.route')),
            ],
            options={
                'ordering': ['created_on'],
            },
        ),
    ]
