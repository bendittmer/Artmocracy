# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('artbase', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='art',
            name='creator',
            field=models.ForeignKey(blank=True, to='artbase.UserProfile', null=True),
            preserve_default=True,
        ),
    ]
