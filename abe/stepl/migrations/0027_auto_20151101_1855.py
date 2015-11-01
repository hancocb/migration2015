# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stepl', '0026_auto_20151031_2305'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gullyerosion',
            name='BMP_Efficiency',
            field=models.FloatField(default=0, choices=[(0, b'0 efficency'), (1, b'1 efficency')]),
        ),
        migrations.AlterField(
            model_name='gullyerosion',
            name='SoilTexture',
            field=models.CharField(default=b'0', max_length=30, choices=[(b'1', b'Clay'), (b'2', b'ClayLoam'), (b'3', b'FineSandyLoam'), (b'4', b'Loams,SandyClayLoams'), (b'5', b'Organic'), (b'6', b'Sands,LoamySands'), (b'7', b'SandyClay'), (b'8', b'SandyLoam'), (b'9', b'SiltLoam'), (b'10', b'SiltyClayLoam,SiltyClay')]),
        ),
        migrations.AlterField(
            model_name='gullyerosioninput',
            name='BMP_Efficiency',
            field=models.FloatField(default=0, choices=[(0, b'0 efficency'), (1, b'1 efficency')]),
        ),
        migrations.AlterField(
            model_name='gullyerosioninput',
            name='SoilTexture',
            field=models.CharField(default=b'0', max_length=30, choices=[(b'1', b'Clay'), (b'2', b'ClayLoam'), (b'3', b'FineSandyLoam'), (b'4', b'Loams,SandyClayLoams'), (b'5', b'Organic'), (b'6', b'Sands,LoamySands'), (b'7', b'SandyClay'), (b'8', b'SandyLoam'), (b'9', b'SiltLoam'), (b'10', b'SiltyClayLoam,SiltyClay')]),
        ),
        migrations.AlterField(
            model_name='soiltexture',
            name='Soil_Textural_Class',
            field=models.CharField(default=b'1', max_length=30, choices=[(b'1', b'Clay'), (b'2', b'ClayLoam'), (b'3', b'FineSandyLoam'), (b'4', b'Loams,SandyClayLoams'), (b'5', b'Organic'), (b'6', b'Sands,LoamySands'), (b'7', b'SandyClay'), (b'8', b'SandyLoam'), (b'9', b'SiltLoam'), (b'10', b'SiltyClayLoam,SiltyClay')]),
        ),
        migrations.AlterField(
            model_name='soiltextureinput',
            name='Soil_Textural_Class',
            field=models.CharField(default=b'1', max_length=30, choices=[(b'1', b'Clay'), (b'2', b'ClayLoam'), (b'3', b'FineSandyLoam'), (b'4', b'Loams,SandyClayLoams'), (b'5', b'Organic'), (b'6', b'Sands,LoamySands'), (b'7', b'SandyClay'), (b'8', b'SandyLoam'), (b'9', b'SiltLoam'), (b'10', b'SiltyClayLoam,SiltyClay')]),
        ),
        migrations.AlterField(
            model_name='streambankerosion',
            name='BMP_Efficiency',
            field=models.FloatField(default=0, choices=[(0, b'0 efficency'), (1, b'1 efficency')]),
        ),
        migrations.AlterField(
            model_name='streambankerosion',
            name='Lateral_Recession',
            field=models.FloatField(default=0, choices=[(1, b'Slight'), (2, b'Moderate'), (3, b'Severe'), (4, b'Very Severe')]),
        ),
        migrations.AlterField(
            model_name='streambankerosion',
            name='SoilTexture',
            field=models.CharField(default=b'0', max_length=30, choices=[(b'1', b'Clay'), (b'2', b'ClayLoam'), (b'3', b'FineSandyLoam'), (b'4', b'Loams,SandyClayLoams'), (b'5', b'Organic'), (b'6', b'Sands,LoamySands'), (b'7', b'SandyClay'), (b'8', b'SandyLoam'), (b'9', b'SiltLoam'), (b'10', b'SiltyClayLoam,SiltyClay')]),
        ),
        migrations.AlterField(
            model_name='streambankerosioninput',
            name='BMP_Efficiency',
            field=models.FloatField(default=0, choices=[(0, b'0 efficency'), (1, b'1 efficency')]),
        ),
        migrations.AlterField(
            model_name='streambankerosioninput',
            name='Lateral_Recession',
            field=models.FloatField(default=0, choices=[(1, b'Slight'), (2, b'Moderate'), (3, b'Severe'), (4, b'Very Severe')]),
        ),
        migrations.AlterField(
            model_name='streambankerosioninput',
            name='SoilTexture',
            field=models.CharField(default=b'0', max_length=30, choices=[(b'1', b'Clay'), (b'2', b'ClayLoam'), (b'3', b'FineSandyLoam'), (b'4', b'Loams,SandyClayLoams'), (b'5', b'Organic'), (b'6', b'Sands,LoamySands'), (b'7', b'SandyClay'), (b'8', b'SandyLoam'), (b'9', b'SiltLoam'), (b'10', b'SiltyClayLoam,SiltyClay')]),
        ),
    ]
