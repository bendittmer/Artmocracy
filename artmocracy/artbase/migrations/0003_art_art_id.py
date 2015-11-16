# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('artbase', '0002_auto_20151009_1816'),
    ]

    operations = [
        migrations.AddField(
            model_name='art',
            name='art_id',
            field=models.IntegerField(default=1),
            preserve_default=True,
        ),
    ]
