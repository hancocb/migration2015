# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stepl', '0017_auto_20151023_1848'),
    ]

    operations = [
        migrations.CreateModel(
            name='BMPInput',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('session_id', models.IntegerField()),
                ('landtype_id', models.IntegerField()),
                ('watershd_id', models.IntegerField()),
                ('BMP', models.IntegerField(default=0)),
                ('PercentApplied', models.FloatField(default=100)),
                ('N', models.FloatField(default=0)),
                ('P', models.FloatField(default=0)),
                ('BOD', models.FloatField(default=0)),
                ('Sediment', models.FloatField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='UrbanBmpInput',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('session_id', models.IntegerField()),
                ('key', models.CharField(max_length=30)),
                ('value', models.FloatField(default=0)),
            ],
        ),
        migrations.AlterUniqueTogether(
            name='urbanbmpinput',
            unique_together=set([('session_id', 'key')]),
        ),
        migrations.AlterUniqueTogether(
            name='bmpinput',
            unique_together=set([('session_id', 'landtype_id', 'watershd_id')]),
        ),
    ]
