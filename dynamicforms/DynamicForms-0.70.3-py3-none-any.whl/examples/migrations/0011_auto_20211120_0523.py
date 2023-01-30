# Generated by Django 3.1.13 on 2021-11-20 05:23

import django.db.models.deletion
import enumfields.fields
from django.db import migrations, models

import examples.recurrence_utils


class Migration(migrations.Migration):

    dependencies = [
        ('examples', '0010_filter_rtf_field'),
    ]

    operations = [
        migrations.CreateModel(
            name='CalendarEvent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=80, verbose_name='Title')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Description')),
                ('colour', models.IntegerField(blank=True, null=True, verbose_name='Colour')),
                ('start_at', models.DateTimeField(verbose_name='Start')),
                ('end_at', models.DateTimeField(verbose_name='End')),
            ],
        ),
        migrations.CreateModel(
            name='CalendarRecurrence',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_at', models.DateTimeField(verbose_name='Recurrence start')),
                ('end_at', models.DateTimeField(verbose_name='Recurrence end')),
                ('pattern',
                 enumfields.fields.EnumIntegerField(enum=examples.recurrence_utils.Pattern, verbose_name='Pattern')),
                ('recur', models.JSONField(verbose_name='Recur parameters')),
            ],
        ),
        migrations.CreateModel(
            name='CalendarReminder',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.IntegerField(choices=[(1, 'Notification'), (2, 'Email')], verbose_name='Type')),
                ('quantity', models.IntegerField(verbose_name='Quantity')),
                ('unit',
                 models.IntegerField(choices=[(1, 'Seconds'), (2, 'Minutes'), (3, 'Hours'), (4, 'Days'), (5, 'Weeks')],
                                     verbose_name='Unit')),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reminders',
                                            to='examples.calendarevent')),
            ],
        ),
        migrations.AddField(
            model_name='calendarevent',
            name='recurrence',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT,
                                    related_name='events', to='examples.calendarrecurrence', verbose_name='Recurrence'),
        ),
        migrations.AddIndex(
            model_name='calendarevent',
            index=models.Index(fields=['recurrence', 'start_at'], name='examples_ca_recurre_f65416_idx'),
        ),
    ]
