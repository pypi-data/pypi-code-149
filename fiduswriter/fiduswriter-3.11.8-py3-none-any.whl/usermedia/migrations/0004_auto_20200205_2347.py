# Generated by Django 2.2.9 on 2020-02-05 22:47

from django.db import migrations, models


def update_cat_field(apps, schema_editor):
    UserImage = apps.get_model("usermedia", "UserImage")
    images = UserImage.objects.all().iterator()
    for image in images:
        image.image_cat = "[" + image.image_cat + "]"
        image.save()


class Migration(migrations.Migration):

    dependencies = [
        ("usermedia", "0003_auto_20200205_2230"),
    ]

    operations = [
        migrations.AlterField(
            model_name="userimage",
            name="image_cat",
            field=models.CharField(default="[]", max_length=255),
        ),
        migrations.RunPython(update_cat_field),
    ]
