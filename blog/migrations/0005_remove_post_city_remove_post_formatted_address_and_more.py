# Generated by Django 4.2.7 on 2023-12-01 14:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("blog", "0004_auto_20231127_2056"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="post",
            name="city",
        ),
        migrations.RemoveField(
            model_name="post",
            name="formatted_address",
        ),
        migrations.RemoveField(
            model_name="post",
            name="street_name",
        ),
        migrations.RemoveField(
            model_name="post",
            name="street_number",
        ),
        migrations.AddField(
            model_name="post",
            name="location",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="post_location",
                to="blog.location",
            ),
        ),
    ]
