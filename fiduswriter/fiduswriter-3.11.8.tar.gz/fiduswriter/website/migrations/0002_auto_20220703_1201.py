# Generated by Django 3.2.13 on 2022-07-03 10:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("website", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="publication",
            name="message_to_editor",
        ),
        migrations.AddField(
            model_name="publication",
            name="messages",
            field=models.JSONField(default=list),
        ),
    ]
