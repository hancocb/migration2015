# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stepl', '0019_auto_20151029_0117'),
    ]

    operations = [
        migrations.AlterField(
            model_name='staticinputmaindata',
            name='Standard',
            field=models.CharField(max_length=30),
        ),
    ]
