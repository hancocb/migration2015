# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stepl', '0008_auto_20151005_1930'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='irrigation',
            name='irrigationabstract_ptr',
        ),
        migrations.AlterUniqueTogether(
            name='irrigationinput',
            unique_together=set([]),
        ),
        migrations.RemoveField(
            model_name='irrigationinput',
            name='irrigationabstract_ptr',
        ),
        migrations.DeleteModel(
            name='Irrigation',
        ),
        migrations.DeleteModel(
            name='IrrigationAbstract',
        ),
        migrations.DeleteModel(
            name='IrrigationInput',
        ),
    ]
