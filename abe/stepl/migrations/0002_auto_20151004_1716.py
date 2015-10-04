# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stepl', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='SoilData',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('Soil_N_Conc', models.FloatField()),
                ('Soil_P_Conc', models.FloatField()),
                ('Soil_BOD_Conc', models.FloatField()),
                ('SHG', models.CharField(unique=True, max_length=10)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='SoilDataInput',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('Soil_N_Conc', models.FloatField()),
                ('Soil_P_Conc', models.FloatField()),
                ('Soil_BOD_Conc', models.FloatField()),
                ('index_id', models.IntegerField()),
                ('watershd_id', models.IntegerField()),
            ],
        ),
        migrations.AlterUniqueTogether(
            name='soildatainput',
            unique_together=set([('index_id', 'watershd_id')]),
        ),
    ]
