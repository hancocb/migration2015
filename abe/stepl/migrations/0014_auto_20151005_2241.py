# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stepl', '0013_auto_20151005_2209'),
    ]

    operations = [
        migrations.AlterField(
            model_name='soiltexture',
            name='Soil_Textural_Class',
            field=models.CharField(default=b'Clay', max_length=30, choices=[(b'Clay', b'Clay'), (b'ClayLoam', b'ClayLoam'), (b'FineSandyLoam', b'FineSandyLoam'), (b'Loams,SandyClayLoams', b'Loams,SandyClayLoams'), (b'Organic', b'Organic'), (b'Sands,LoamySands', b'Sands,LoamySands'), (b'SandyClay', b'SandyClay'), (b'SandyLoam', b'SandyLoam'), (b'SiltLoam', b'SiltLoam'), (b'SiltyClayLoam,SiltyClay', b'SiltyClayLoam,SiltyClay')]),
        ),
        migrations.AlterField(
            model_name='soiltextureinput',
            name='Soil_Textural_Class',
            field=models.CharField(default=b'Clay', max_length=30, choices=[(b'Clay', b'Clay'), (b'ClayLoam', b'ClayLoam'), (b'FineSandyLoam', b'FineSandyLoam'), (b'Loams,SandyClayLoams', b'Loams,SandyClayLoams'), (b'Organic', b'Organic'), (b'Sands,LoamySands', b'Sands,LoamySands'), (b'SandyClay', b'SandyClay'), (b'SandyLoam', b'SandyLoam'), (b'SiltLoam', b'SiltLoam'), (b'SiltyClayLoam,SiltyClay', b'SiltyClayLoam,SiltyClay')]),
        ),
    ]
