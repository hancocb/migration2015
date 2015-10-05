# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stepl', '0006_auto_20151005_1924'),
    ]

    operations = [
        migrations.RenameField(
            model_name='urbanreferencerunoff',
            old_name='Urban',
            new_name='Landuse',
        ),
        migrations.RenameField(
            model_name='urbanreferencerunoffinput',
            old_name='Urban',
            new_name='Landuse',
        ),
        migrations.AlterUniqueTogether(
            name='urbanreferencerunoffinput',
            unique_together=set([('session_id', 'Landuse')]),
        ),
    ]
