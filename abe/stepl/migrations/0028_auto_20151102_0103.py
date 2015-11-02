# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stepl', '0027_auto_20151101_1855'),
    ]

    operations = [
        migrations.AddField(
            model_name='countydatainput',
            name='LocFileName',
            field=models.CharField(default='', max_length=30),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='countydatainput',
            name='LocName',
            field=models.CharField(default='', max_length=30),
            preserve_default=False,
        ),
    ]
