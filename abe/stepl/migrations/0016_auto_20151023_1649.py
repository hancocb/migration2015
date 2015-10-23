# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stepl', '0015_auto_20151006_2118'),
    ]

    operations = [
        migrations.AddField(
            model_name='indexinput',
            name='gwOpt',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='indexinput',
            name='swsOpt',
            field=models.BooleanField(default=True),
        ),
    ]
