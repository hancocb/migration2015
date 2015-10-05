# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stepl', '0009_auto_20151005_1942'),
    ]

    operations = [
        migrations.CreateModel(
            name='Irrigation',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('Cropland_Acres_Irrigated', models.FloatField()),
                ('Water_Depth_in_per_Irrigation_Before_BMP', models.FloatField()),
                ('Water_Depth_in_per_Irrigation_After_BMP', models.FloatField()),
                ('Irrigation_Frequency_perYear', models.FloatField()),
                ('Standard', models.CharField(unique=True, max_length=30)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='IrrigationInput',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('Cropland_Acres_Irrigated', models.FloatField()),
                ('Water_Depth_in_per_Irrigation_Before_BMP', models.FloatField()),
                ('Water_Depth_in_per_Irrigation_After_BMP', models.FloatField()),
                ('Irrigation_Frequency_perYear', models.FloatField()),
                ('session_id', models.IntegerField()),
                ('watershd_id', models.IntegerField()),
            ],
        ),
        migrations.AlterUniqueTogether(
            name='irrigationinput',
            unique_together=set([('session_id', 'watershd_id')]),
        ),
    ]
