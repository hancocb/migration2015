# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stepl', '0004_urbanreferencerunoff_urbanreferencerunoffinput'),
    ]

    operations = [
        migrations.AlterField(
            model_name='urbanreferencerunoffinput',
            name='session_id',
            field=models.IntegerField(),
        ),
        migrations.AlterUniqueTogether(
            name='urbanreferencerunoffinput',
            unique_together=set([('session_id', 'Urban')]),
        ),
    ]
