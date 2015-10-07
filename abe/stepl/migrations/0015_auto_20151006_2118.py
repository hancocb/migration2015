# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stepl', '0014_auto_20151005_2241'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gullyerosion',
            name='SoilTexture',
            field=models.CharField(default=b'Clay', max_length=30, choices=[(b'Clay', b'Clay'), (b'ClayLoam', b'ClayLoam'), (b'FineSandyLoam', b'FineSandyLoam'), (b'Loams,SandyClayLoams', b'Loams,SandyClayLoams'), (b'Organic', b'Organic'), (b'Sands,LoamySands', b'Sands,LoamySands'), (b'SandyClay', b'SandyClay'), (b'SandyLoam', b'SandyLoam'), (b'SiltLoam', b'SiltLoam'), (b'SiltyClayLoam,SiltyClay', b'SiltyClayLoam,SiltyClay')]),
        ),
        migrations.AlterField(
            model_name='gullyerosioninput',
            name='SoilTexture',
            field=models.CharField(default=b'Clay', max_length=30, choices=[(b'Clay', b'Clay'), (b'ClayLoam', b'ClayLoam'), (b'FineSandyLoam', b'FineSandyLoam'), (b'Loams,SandyClayLoams', b'Loams,SandyClayLoams'), (b'Organic', b'Organic'), (b'Sands,LoamySands', b'Sands,LoamySands'), (b'SandyClay', b'SandyClay'), (b'SandyLoam', b'SandyLoam'), (b'SiltLoam', b'SiltLoam'), (b'SiltyClayLoam,SiltyClay', b'SiltyClayLoam,SiltyClay')]),
        ),
        migrations.AlterField(
            model_name='streambankerosion',
            name='SoilTexture',
            field=models.CharField(default=b'Clay', max_length=30, choices=[(b'Clay', b'Clay'), (b'ClayLoam', b'ClayLoam'), (b'FineSandyLoam', b'FineSandyLoam'), (b'Loams,SandyClayLoams', b'Loams,SandyClayLoams'), (b'Organic', b'Organic'), (b'Sands,LoamySands', b'Sands,LoamySands'), (b'SandyClay', b'SandyClay'), (b'SandyLoam', b'SandyLoam'), (b'SiltLoam', b'SiltLoam'), (b'SiltyClayLoam,SiltyClay', b'SiltyClayLoam,SiltyClay')]),
        ),
        migrations.AlterField(
            model_name='streambankerosioninput',
            name='SoilTexture',
            field=models.CharField(default=b'Clay', max_length=30, choices=[(b'Clay', b'Clay'), (b'ClayLoam', b'ClayLoam'), (b'FineSandyLoam', b'FineSandyLoam'), (b'Loams,SandyClayLoams', b'Loams,SandyClayLoams'), (b'Organic', b'Organic'), (b'Sands,LoamySands', b'Sands,LoamySands'), (b'SandyClay', b'SandyClay'), (b'SandyLoam', b'SandyLoam'), (b'SiltLoam', b'SiltLoam'), (b'SiltyClayLoam,SiltyClay', b'SiltyClayLoam,SiltyClay')]),
        ),
    ]
