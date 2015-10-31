# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stepl', '0020_auto_20151029_0145'),
    ]

    operations = [
        migrations.DeleteModel(
            name='StaticInputMainData',
        ),
        migrations.DeleteModel(
            name='StaticInputMainInput',
        ),
    ]
