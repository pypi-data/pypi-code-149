# Generated by Django 2.2 on 2021-02-08 05:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("events", "0002_add_climatecare_fields"),
    ]

    operations = [
        migrations.AlterField(
            model_name="event",
            name="address",
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name="event",
            name="tags",
            field=models.ManyToManyField(
                blank=True,
                related_name="events_event_tags",
                to="events.Tag",
                verbose_name="Tags",
            ),
        ),
    ]
