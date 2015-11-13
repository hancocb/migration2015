# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stepl', '0029_auto_20151112_2055'),
    ]

    operations = [
        migrations.AlterField(
            model_name='streambankerosion',
            name='Lateral_Recession',
            field=models.IntegerField(default=0, choices=[(1, b'Slight'), (2, b'Moderate'), (3, b'Severe'), (4, b'Very Severe')]),
        ),
        migrations.AlterField(
            model_name='streambankerosioninput',
            name='Lateral_Recession',
            field=models.IntegerField(default=0, choices=[(1, b'Slight'), (2, b'Moderate'), (3, b'Severe'), (4, b'Very Severe')]),
        ),
    ]
