# Generated by Django 5.0 on 2023-12-13 21:56

import django_google_maps.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_remove_post_location'),
    ]

    operations = [
        migrations.AddField(
            model_name='location',
            name='address',
            field=django_google_maps.fields.AddressField(default=False, max_length=200),
        ),
        migrations.AddField(
            model_name='location',
            name='geolocation',
            field=django_google_maps.fields.GeoLocationField(default=False, max_length=100),
        ),
    ]
