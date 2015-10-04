# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stepl', '0002_auto_20151004_1716'),
    ]

    operations = [
        migrations.RenameField(
            model_name='countydatainput',
            old_name='index_id',
            new_name='session_id',
        ),
        migrations.RenameField(
            model_name='soildatainput',
            old_name='index_id',
            new_name='session_id',
        ),
        migrations.AlterUniqueTogether(
            name='soildatainput',
            unique_together=set([('session_id', 'watershd_id')]),
        ),
    ]
