# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import artbase.models


class Migration(migrations.Migration):

    dependencies = [
        ('artbase', '0004_art_art_votes'),
    ]

    operations = [
        migrations.CreateModel(
            name='Picture',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('file', models.ImageField(upload_to=artbase.models.get_upload_path)),
            ],
        ),
    ]
