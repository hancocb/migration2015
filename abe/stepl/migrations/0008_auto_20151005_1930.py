# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stepl', '0007_auto_20151005_1925'),
    ]

    operations = [
        migrations.RenameField(
            model_name='irrigation',
            old_name='Type',
            new_name='Standard',
        ),
        migrations.RenameField(
            model_name='landusedistribution',
            old_name='Type',
            new_name='Standard',
        ),
        migrations.RenameField(
            model_name='soildata',
            old_name='SHG',
            new_name='Standard',
        ),
    ]
