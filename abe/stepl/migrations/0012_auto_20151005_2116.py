# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stepl', '0011_auto_20151005_2011'),
    ]

    operations = [
        migrations.CreateModel(
            name='SoilInfiltrationFraction',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('HSG', models.CharField(default=b'', max_length=30, db_index=True)),
                ('A', models.FloatField(default=0)),
                ('B', models.FloatField(default=0)),
                ('C', models.FloatField(default=0)),
                ('D', models.FloatField(default=0)),
                ('Standard', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='SoilInfiltrationFractionInput',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('HSG', models.CharField(default=b'', max_length=30, db_index=True)),
                ('A', models.FloatField(default=0)),
                ('B', models.FloatField(default=0)),
                ('C', models.FloatField(default=0)),
                ('D', models.FloatField(default=0)),
                ('session_id', models.IntegerField()),
            ],
        ),
        migrations.AlterUniqueTogether(
            name='soilinfiltrationfractioninput',
            unique_together=set([('session_id', 'HSG')]),
        ),
        migrations.AlterUniqueTogether(
            name='soilinfiltrationfraction',
            unique_together=set([('Standard', 'HSG')]),
        ),
    ]
