# Generated by Django 5.0 on 2023-12-14 08:52

import django_google_maps.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_location_address_location_geolocation'),
    ]

    operations = [
        migrations.AlterField(
            model_name='location',
            name='address',
            field=django_google_maps.fields.AddressField(max_length=200),
        ),
    ]