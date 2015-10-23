# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stepl', '0016_auto_20151023_1649'),
    ]

    operations = [
        migrations.CreateModel(
            name='AgriAnimal',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('watershd_id', models.IntegerField()),
                ('Beef', models.IntegerField(default=0)),
                ('Dairy', models.IntegerField(default=0)),
                ('Swine', models.IntegerField(default=0)),
                ('Sheep', models.IntegerField(default=0)),
                ('Horse', models.IntegerField(default=0)),
                ('Chicken', models.IntegerField(default=0)),
                ('Turkey', models.IntegerField(default=0)),
                ('Duck', models.IntegerField(default=0)),
                ('numMonthsManureApplied', models.IntegerField(default=0)),
                ('session_id', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='SepticNillegal',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('watershd_id', models.IntegerField()),
                ('numSepticSystems', models.IntegerField(default=0)),
                ('PopulationPerSeptic', models.IntegerField(default=0)),
                ('SepticFailureRate_Percent', models.IntegerField(default=0)),
                ('Wastewater_Direct_Discharge_numPeople', models.IntegerField(default=0)),
                ('Direct_Discharge_Reduction_Percent', models.IntegerField(default=0)),
                ('session_id', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='WatershedLandUse',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('watershd_id', models.IntegerField()),
                ('HSG', models.IntegerField(default=1)),
                ('Urban', models.FloatField(default=0)),
                ('Cropland', models.FloatField(default=0)),
                ('Pastureland', models.FloatField(default=0)),
                ('Forest', models.FloatField(default=0)),
                ('UserDefined', models.FloatField(default=0)),
                ('Feedlots', models.FloatField(default=0)),
                ('FeedlotPercentPaved', models.IntegerField(default=20)),
                ('Total', models.FloatField(default=0)),
                ('session_id', models.IntegerField()),
            ],
        ),
        migrations.AlterUniqueTogether(
            name='watershedlanduse',
            unique_together=set([('session_id', 'watershd_id')]),
        ),
        migrations.AlterUniqueTogether(
            name='septicnillegal',
            unique_together=set([('session_id', 'watershd_id')]),
        ),
        migrations.AlterUniqueTogether(
            name='agrianimal',
            unique_together=set([('session_id', 'watershd_id')]),
        ),
    ]
