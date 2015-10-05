# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stepl', '0003_auto_20151004_1828'),
    ]

    operations = [
        migrations.CreateModel(
            name='UrbanReferenceRunoff',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('SHG_A', models.IntegerField()),
                ('SHG_B', models.IntegerField()),
                ('SHG_C', models.IntegerField()),
                ('SHG_D', models.IntegerField()),
                ('Urban', models.CharField(unique=True, max_length=10)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='UrbanReferenceRunoffInput',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('SHG_A', models.IntegerField()),
                ('SHG_B', models.IntegerField()),
                ('SHG_C', models.IntegerField()),
                ('SHG_D', models.IntegerField()),
                ('Urban', models.CharField(max_length=10, db_index=True)),
                ('session_id', models.IntegerField(unique=True)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
