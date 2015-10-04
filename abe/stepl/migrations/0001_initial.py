# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CountyData',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('state_name', models.CharField(max_length=30)),
                ('name', models.CharField(max_length=30)),
                ('rmean', models.FloatField(null=True)),
                ('kmean', models.FloatField(null=True)),
                ('lsavg', models.FloatField(null=True)),
                ('cavg', models.FloatField(null=True)),
                ('pavg', models.FloatField(null=True)),
                ('state_name_name', models.CharField(max_length=30)),
                ('rainfall_inches', models.FloatField()),
                ('raindays', models.FloatField()),
                ('runoff', models.FloatField()),
                ('station_name', models.CharField(max_length=30, null=True)),
                ('ptrecipitation_correction_factor', models.FloatField(null=True)),
                ('no_of_rain_days_correction_factor', models.FloatField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='CountyDataInput',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('state_name', models.CharField(max_length=30)),
                ('name', models.CharField(max_length=30)),
                ('rmean', models.FloatField(null=True)),
                ('kmean', models.FloatField(null=True)),
                ('lsavg', models.FloatField(null=True)),
                ('cavg', models.FloatField(null=True)),
                ('pavg', models.FloatField(null=True)),
                ('index_id', models.IntegerField(unique=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='IndexInput',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('num_watershd', models.IntegerField()),
                ('num_gully', models.IntegerField()),
                ('num_steambank', models.IntegerField()),
            ],
        ),
        migrations.AlterUniqueTogether(
            name='countydata',
            unique_together=set([('state_name', 'name')]),
        ),
    ]
