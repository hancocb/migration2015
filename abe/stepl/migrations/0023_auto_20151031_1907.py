# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stepl', '0022_auto_20151031_1817'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='UrbanReferenceRunoff',
            new_name='ReferenceRunoff',
        ),
        migrations.RenameModel(
            old_name='UrbanReferenceRunoffInput',
            new_name='ReferenceRunoffInput',
        ),
    ]
