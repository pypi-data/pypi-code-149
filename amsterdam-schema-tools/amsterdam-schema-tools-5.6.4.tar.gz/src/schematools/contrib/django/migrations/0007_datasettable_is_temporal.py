# Generated by Django 3.0.7 on 2020-09-01 13:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("datasets", "0006_remote_datasets"),
    ]

    operations = [
        migrations.AddField(
            model_name="datasettable",
            name="is_temporal",
            field=models.BooleanField(default=False),
        ),
    ]
