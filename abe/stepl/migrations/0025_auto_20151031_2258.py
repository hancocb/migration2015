# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stepl', '0024_auto_20151031_2045'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lateralrecessionrate',
            name='LRR',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='lateralrecessionrateinput',
            name='LRR',
            field=models.CharField(max_length=30),
        ),
    ]
