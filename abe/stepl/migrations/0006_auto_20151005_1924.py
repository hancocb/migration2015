# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stepl', '0005_auto_20151005_1626'),
    ]

    operations = [
        migrations.CreateModel(
            name='DetailedRunoff',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('SHG_A', models.IntegerField()),
                ('SHG_B', models.IntegerField()),
                ('SHG_C', models.IntegerField()),
                ('SHG_D', models.IntegerField()),
                ('Landuse', models.CharField(unique=True, max_length=30)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='DetailedRunoffInput',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('SHG_A', models.IntegerField()),
                ('SHG_B', models.IntegerField()),
                ('SHG_C', models.IntegerField()),
                ('SHG_D', models.IntegerField()),
                ('Landuse', models.CharField(max_length=30, db_index=True)),
                ('session_id', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='IrrigationAbstract',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('Cropland_Acres_Irrigated', models.FloatField()),
                ('Water_Depth_in_per_Irrigation_Before_BMP', models.FloatField()),
                ('Water_Depth_in_per_Irrigation_After_BMP', models.FloatField()),
                ('Irrigation_Frequency_perYear', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='LanduseDistribution',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('Commercial', models.FloatField()),
                ('Industrial', models.FloatField()),
                ('Institutional', models.FloatField()),
                ('Transportation', models.FloatField()),
                ('Multi_Family', models.FloatField()),
                ('Single_Family', models.FloatField()),
                ('Urban_Cultivated', models.FloatField()),
                ('Vacant_developed', models.FloatField()),
                ('Open_Space', models.FloatField()),
                ('Total', models.FloatField()),
                ('Type', models.CharField(unique=True, max_length=30)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='LanduseDistributionInput',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('Commercial', models.FloatField()),
                ('Industrial', models.FloatField()),
                ('Institutional', models.FloatField()),
                ('Transportation', models.FloatField()),
                ('Multi_Family', models.FloatField()),
                ('Single_Family', models.FloatField()),
                ('Urban_Cultivated', models.FloatField()),
                ('Vacant_developed', models.FloatField()),
                ('Open_Space', models.FloatField()),
                ('Total', models.FloatField()),
                ('session_id', models.IntegerField()),
                ('watershd_id', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='NutrientGroundwaterRunoff',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('N', models.FloatField()),
                ('P', models.FloatField()),
                ('BOD', models.FloatField()),
                ('Landuse', models.CharField(unique=True, max_length=30)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='NutrientGroundwaterRunoffInput',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('N', models.FloatField()),
                ('P', models.FloatField()),
                ('BOD', models.FloatField()),
                ('Landuse', models.CharField(max_length=30, db_index=True)),
                ('session_id', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='NutrientRunoff',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('N', models.FloatField()),
                ('P', models.FloatField()),
                ('BOD', models.FloatField()),
                ('Landuse', models.CharField(unique=True, max_length=30)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='NutrientRunoffInput',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('N', models.FloatField()),
                ('P', models.FloatField()),
                ('BOD', models.FloatField()),
                ('Landuse', models.CharField(max_length=30, db_index=True)),
                ('session_id', models.IntegerField()),
            ],
        ),
        migrations.AlterField(
            model_name='soildata',
            name='SHG',
            field=models.CharField(unique=True, max_length=30),
        ),
        migrations.AlterField(
            model_name='urbanreferencerunoff',
            name='Urban',
            field=models.CharField(unique=True, max_length=30),
        ),
        migrations.AlterField(
            model_name='urbanreferencerunoffinput',
            name='Urban',
            field=models.CharField(max_length=30, db_index=True),
        ),
        migrations.CreateModel(
            name='Irrigation',
            fields=[
                ('irrigationabstract_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='stepl.IrrigationAbstract')),
                ('Type', models.CharField(unique=True, max_length=30)),
            ],
            bases=('stepl.irrigationabstract',),
        ),
        migrations.CreateModel(
            name='IrrigationInput',
            fields=[
                ('irrigationabstract_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='stepl.IrrigationAbstract')),
                ('session_id', models.IntegerField()),
                ('watershd_id', models.IntegerField()),
            ],
            bases=('stepl.irrigationabstract',),
        ),
        migrations.AlterUniqueTogether(
            name='nutrientrunoffinput',
            unique_together=set([('session_id', 'Landuse')]),
        ),
        migrations.AlterUniqueTogether(
            name='nutrientgroundwaterrunoffinput',
            unique_together=set([('session_id', 'Landuse')]),
        ),
        migrations.AlterUniqueTogether(
            name='landusedistributioninput',
            unique_together=set([('session_id', 'watershd_id')]),
        ),
        migrations.AlterUniqueTogether(
            name='detailedrunoffinput',
            unique_together=set([('session_id', 'Landuse')]),
        ),
        migrations.AlterUniqueTogether(
            name='irrigationinput',
            unique_together=set([('session_id', 'watershd_id')]),
        ),
    ]
