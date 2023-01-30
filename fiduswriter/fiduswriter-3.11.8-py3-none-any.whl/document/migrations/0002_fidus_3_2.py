# Generated by Django 2.2.9 on 2020-02-05 17:27
import os
import zipfile
import tempfile
from decimal import Decimal

from django.db import migrations, models
from django.core.files import File

# FW 3.1 documents can be upgraded to 3.2 without changes
# (not true for reverse conversion)
OLD_FW_DOCUMENT_VERSION = 3.1
FW_DOCUMENT_VERSION = 3.2


# from https://stackoverflow.com/questions/25738523/how-to-update-one-file-inside-zip-file-using-python
def update_revision_zip(file_field, file_name):
    # generate a temp file
    tmpfd, tmpname = tempfile.mkstemp()
    os.close(tmpfd)
    # create a temp copy of the archive without filename
    with zipfile.ZipFile(file_field.open(), "r") as zin:
        with zipfile.ZipFile(tmpname, "w") as zout:
            zout.comment = zin.comment  # preserve the comment
            for item in zin.infolist():
                if item.filename == "filetype-version":
                    zout.writestr(item, str(FW_DOCUMENT_VERSION))
                else:
                    zout.writestr(item, zin.read(item.filename))
    # replace with the temp archive
    with open(tmpname, "rb") as tmp_file:
        file_field.save(file_name, File(tmp_file))
    os.remove(tmpname)


def set_document_version(apps, schema_editor):
    Document = apps.get_model("document", "Document")
    documents = Document.objects.all().iterator()
    for document in documents:
        if document.doc_version == Decimal(str(OLD_FW_DOCUMENT_VERSION)):
            document.doc_version = FW_DOCUMENT_VERSION
            for field in document._meta.local_fields:
                if field.name == "updated":
                    field.auto_now = False
            document.save()

    DocumentTemplate = apps.get_model("document", "DocumentTemplate")
    templates = DocumentTemplate.objects.all()
    for template in templates:
        if template.doc_version == Decimal(str(OLD_FW_DOCUMENT_VERSION)):
            template.doc_version = FW_DOCUMENT_VERSION
            template.save()

    DocumentRevision = apps.get_model("document", "DocumentRevision")
    revisions = DocumentRevision.objects.all()
    for revision in revisions:
        if not revision.file_object:
            revision.delete()
            continue
        if revision.doc_version == Decimal(str(OLD_FW_DOCUMENT_VERSION)):
            revision.doc_version = FW_DOCUMENT_VERSION
            revision.save()
            # Set the version number also in the zip file.
            update_revision_zip(revision.file_object, revision.file_name)


class Migration(migrations.Migration):

    dependencies = [
        ("document", "0001_squashed_20200219"),
    ]

    operations = [
        migrations.AlterField(
            model_name="document",
            name="doc_version",
            field=models.DecimalField(
                decimal_places=1, default=3.2, max_digits=3
            ),
        ),
        migrations.AlterField(
            model_name="documentrevision",
            name="doc_version",
            field=models.DecimalField(
                decimal_places=1, default=3.2, max_digits=3
            ),
        ),
        migrations.AlterField(
            model_name="documenttemplate",
            name="doc_version",
            field=models.DecimalField(
                decimal_places=1, default=3.2, max_digits=3
            ),
        ),
        migrations.RunPython(set_document_version),
    ]
