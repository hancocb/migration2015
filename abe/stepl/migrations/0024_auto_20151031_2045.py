# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stepl', '0023_auto_20151031_1907'),
    ]

    operations = [
        migrations.AddField(
            model_name='detailedrunoff',
            name='Standard',
            field=models.CharField(default='A', max_length=30),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='nutrientgroundwaterrunoff',
            name='Standard',
            field=models.CharField(default=b'A', max_length=30),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='nutrientrunoff',
            name='Standard',
            field=models.CharField(default=1, max_length=30),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='referencerunoff',
            name='Standard',
            field=models.CharField(default='A', max_length=30),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='detailedrunoff',
            name='Urban',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='nutrientgroundwaterrunoff',
            name='Landuse',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='nutrientrunoff',
            name='Landuse',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='referencerunoff',
            name='Landuse',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterUniqueTogether(
            name='detailedrunoff',
            unique_together=set([('Standard', 'Urban')]),
        ),
        migrations.AlterUniqueTogether(
            name='nutrientgroundwaterrunoff',
            unique_together=set([('Standard', 'Landuse')]),
        ),
        migrations.AlterUniqueTogether(
            name='nutrientrunoff',
            unique_together=set([('Standard', 'Landuse')]),
        ),
        migrations.AlterUniqueTogether(
            name='referencerunoff',
            unique_together=set([('Standard', 'Landuse')]),
        ),
    ]
