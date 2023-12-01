# Generated by Django 4.2.7 on 2023-12-01 17:02

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("blog", "0001_initial"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="comments",
            options={},
        ),
        migrations.RemoveField(
            model_name="comments",
            name="created_on",
        ),
        migrations.AlterField(
            model_name="comments",
            name="author",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="author",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
    ]
