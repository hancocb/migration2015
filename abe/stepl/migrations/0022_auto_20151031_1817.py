# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stepl', '0021_auto_20151029_0217'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='FreelotAnimal',
            new_name='FeedlotAnimal',
        ),
        migrations.RenameModel(
            old_name='FreelotAnimalInput',
            new_name='FeedlotAnimalInput',
        ),
    ]
