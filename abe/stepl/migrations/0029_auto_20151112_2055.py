# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stepl', '0028_auto_20151102_0103'),
    ]

    operations = [
        migrations.CreateModel(
            name='UniversalSoilLossEquation',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('watershd_id', models.IntegerField()),
                ('Cropland_R', models.FloatField(default=0)),
                ('Cropland_K', models.FloatField(default=0)),
                ('Cropland_LS', models.FloatField(default=0)),
                ('Cropland_C', models.FloatField(default=0)),
                ('Cropland_P', models.FloatField(default=0)),
                ('Pastureland_R', models.FloatField(default=0)),
                ('Pastureland_K', models.FloatField(default=0)),
                ('Pastureland_LS', models.FloatField(default=0)),
                ('Pastureland_C', models.FloatField(default=0)),
                ('Pastureland_P', models.FloatField(default=0)),
                ('Forest_R', models.FloatField(default=0)),
                ('Forest_K', models.FloatField(default=0)),
                ('Forest_LS', models.FloatField(default=0)),
                ('Forest_C', models.FloatField(default=0)),
                ('Forest_P', models.FloatField(default=0)),
                ('UserDefined_R', models.FloatField(default=0)),
                ('UserDefined_K', models.FloatField(default=0)),
                ('UserDefined_LS', models.FloatField(default=0)),
                ('UserDefined_C', models.FloatField(default=0)),
                ('UserDefined_P', models.FloatField(default=0)),
                ('session_id', models.IntegerField()),
            ],
        ),
        migrations.AlterUniqueTogether(
            name='universalsoillossequation',
            unique_together=set([('session_id', 'watershd_id')]),
        ),
    ]
