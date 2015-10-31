# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stepl', '0018_auto_20151029_0056'),
    ]

    operations = [
        migrations.CreateModel(
            name='StaticInputMainData',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('Standard', models.CharField(unique=True, max_length=30)),
                ('key', models.CharField(max_length=30)),
                ('value', models.FloatField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='StaticInputMainInput',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('session_id', models.IntegerField()),
                ('key', models.CharField(max_length=30)),
                ('value', models.FloatField(default=0)),
            ],
        ),
        migrations.AlterUniqueTogether(
            name='staticinputmaininput',
            unique_together=set([('session_id', 'key')]),
        ),
        migrations.AlterUniqueTogether(
            name='staticinputmaindata',
            unique_together=set([('Standard', 'key')]),
        ),
    ]
