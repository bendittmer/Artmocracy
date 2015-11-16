# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('artbase', '0005_picture'),
    ]

    operations = [
        migrations.AddField(
            model_name='picture',
            name='pic_id',
            field=models.IntegerField(default=0),
        ),
    ]
