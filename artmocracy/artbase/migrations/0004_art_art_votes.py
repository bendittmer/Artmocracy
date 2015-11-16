# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('artbase', '0003_art_art_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='art',
            name='art_votes',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
    ]
