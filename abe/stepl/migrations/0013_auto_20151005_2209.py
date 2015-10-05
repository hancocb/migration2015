# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stepl', '0012_auto_20151005_2116'),
    ]

    operations = [
        migrations.CreateModel(
            name='AnimalWeight',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('Animal', models.CharField(default=b'', max_length=30)),
                ('MassLb', models.FloatField(default=0)),
                ('BOD_per_1000lb', models.FloatField(default=0)),
                ('BOD_per_day', models.FloatField(default=0)),
                ('BDO_per_year', models.FloatField(default=0)),
                ('Standard', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='AnimalWeightInput',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('Animal', models.CharField(default=b'', max_length=30)),
                ('MassLb', models.FloatField(default=0)),
                ('BOD_per_1000lb', models.FloatField(default=0)),
                ('BOD_per_day', models.FloatField(default=0)),
                ('BDO_per_year', models.FloatField(default=0)),
                ('session_id', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='FreelotAnimal',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('Animal', models.CharField(default=b'', max_length=30)),
                ('N', models.FloatField(default=0)),
                ('P', models.FloatField(default=0)),
                ('BOD', models.FloatField(default=0)),
                ('COD', models.FloatField(default=0)),
                ('Standard', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='FreelotAnimalInput',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('Animal', models.CharField(default=b'', max_length=30)),
                ('N', models.FloatField(default=0)),
                ('P', models.FloatField(default=0)),
                ('BOD', models.FloatField(default=0)),
                ('COD', models.FloatField(default=0)),
                ('session_id', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='GullyErosion',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('SoilTexture', models.CharField(default=b'', max_length=30)),
                ('BMP_Efficiency', models.FloatField(default=0)),
                ('Years_to_Form', models.FloatField(default=0)),
                ('Length', models.FloatField(default=0)),
                ('Depth', models.FloatField(default=0)),
                ('Bottom_Width', models.FloatField(default=0)),
                ('Top_Width', models.FloatField(default=0)),
                ('Standard', models.CharField(unique=True, max_length=30)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='GullyErosionInput',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('SoilTexture', models.CharField(default=b'', max_length=30)),
                ('BMP_Efficiency', models.FloatField(default=0)),
                ('Years_to_Form', models.FloatField(default=0)),
                ('Length', models.FloatField(default=0)),
                ('Depth', models.FloatField(default=0)),
                ('Bottom_Width', models.FloatField(default=0)),
                ('Top_Width', models.FloatField(default=0)),
                ('session_id', models.IntegerField()),
                ('Gully_id', models.IntegerField()),
                ('watershd_id', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='LateralRecessionRate',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('Category', models.CharField(default=b'', max_length=30)),
                ('LRR', models.FloatField(default=0)),
                ('Medium_Value', models.FloatField(default=0)),
                ('Standard', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='LateralRecessionRateInput',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('Category', models.CharField(default=b'', max_length=30)),
                ('LRR', models.FloatField(default=0)),
                ('Medium_Value', models.FloatField(default=0)),
                ('session_id', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='SepticSystem',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('Title', models.CharField(default=b'', max_length=30)),
                ('ACR', models.FloatField(default=0)),
                ('Wastewater_per_capita', models.FloatField(default=0)),
                ('Standard', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='SepticSystemInput',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('Title', models.CharField(default=b'', max_length=30)),
                ('ACR', models.FloatField(default=0)),
                ('Wastewater_per_capita', models.FloatField(default=0)),
                ('session_id', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='SoilTexture',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('Soil_Textural_Class', models.CharField(default=b'', max_length=30)),
                ('Dry_Density', models.FloatField(default=0)),
                ('Correction_Factor', models.FloatField(default=0)),
                ('Standard', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='SoilTextureInput',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('Soil_Textural_Class', models.CharField(default=b'', max_length=30)),
                ('Dry_Density', models.FloatField(default=0)),
                ('Correction_Factor', models.FloatField(default=0)),
                ('session_id', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='StreambankErosion',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('SoilTexture', models.CharField(default=b'', max_length=30)),
                ('BMP_Efficiency', models.FloatField(default=0)),
                ('Lateral_Recession', models.FloatField(default=0)),
                ('Length', models.FloatField(default=0)),
                ('Height', models.FloatField(default=0)),
                ('Standard', models.CharField(unique=True, max_length=30)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='StreambankErosionInput',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('SoilTexture', models.CharField(default=b'', max_length=30)),
                ('BMP_Efficiency', models.FloatField(default=0)),
                ('Lateral_Recession', models.FloatField(default=0)),
                ('Length', models.FloatField(default=0)),
                ('Height', models.FloatField(default=0)),
                ('session_id', models.IntegerField()),
                ('Streambank_id', models.IntegerField()),
                ('watershd_id', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='WildlifeDensityInCropLand',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('Wildlife', models.CharField(default=b'', max_length=30)),
                ('NumPerMileSquare', models.IntegerField(default=0)),
                ('Standard', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='WildlifeDensityInCropLandInput',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('Wildlife', models.CharField(default=b'', max_length=30)),
                ('NumPerMileSquare', models.IntegerField(default=0)),
                ('session_id', models.IntegerField()),
            ],
        ),
        migrations.AlterUniqueTogether(
            name='wildlifedensityincroplandinput',
            unique_together=set([('session_id', 'Wildlife')]),
        ),
        migrations.AlterUniqueTogether(
            name='wildlifedensityincropland',
            unique_together=set([('Standard', 'Wildlife')]),
        ),
        migrations.AlterUniqueTogether(
            name='streambankerosioninput',
            unique_together=set([('session_id', 'Streambank_id')]),
        ),
        migrations.AlterUniqueTogether(
            name='soiltextureinput',
            unique_together=set([('session_id', 'Soil_Textural_Class')]),
        ),
        migrations.AlterUniqueTogether(
            name='soiltexture',
            unique_together=set([('Standard', 'Soil_Textural_Class')]),
        ),
        migrations.AlterUniqueTogether(
            name='septicsysteminput',
            unique_together=set([('session_id', 'Title')]),
        ),
        migrations.AlterUniqueTogether(
            name='septicsystem',
            unique_together=set([('Standard', 'Title')]),
        ),
        migrations.AlterUniqueTogether(
            name='lateralrecessionrateinput',
            unique_together=set([('session_id', 'Category')]),
        ),
        migrations.AlterUniqueTogether(
            name='lateralrecessionrate',
            unique_together=set([('Standard', 'Category')]),
        ),
        migrations.AlterUniqueTogether(
            name='gullyerosioninput',
            unique_together=set([('session_id', 'Gully_id')]),
        ),
        migrations.AlterUniqueTogether(
            name='freelotanimalinput',
            unique_together=set([('session_id', 'Animal')]),
        ),
        migrations.AlterUniqueTogether(
            name='freelotanimal',
            unique_together=set([('Standard', 'Animal')]),
        ),
        migrations.AlterUniqueTogether(
            name='animalweightinput',
            unique_together=set([('session_id', 'Animal')]),
        ),
        migrations.AlterUniqueTogether(
            name='animalweight',
            unique_together=set([('Standard', 'Animal')]),
        ),
    ]
