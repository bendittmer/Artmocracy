# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Art',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('category', models.CharField(max_length=15)),
                ('text', models.TextField()),
                ('submission_date', models.DateTimeField(default=django.utils.timezone.now, verbose_name='submission date', blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('gold', models.IntegerField(default=50)),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='WinningArt',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('category', models.CharField(max_length=15)),
                ('text', models.TextField()),
                ('submission_date', models.DateTimeField(default=django.utils.timezone.now, verbose_name='submission date', blank=True)),
                ('creator', models.ForeignKey(to='artbase.UserProfile')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='art',
            name='creator',
            field=models.ForeignKey(to='artbase.UserProfile'),
            preserve_default=True,
        ),
    ]
