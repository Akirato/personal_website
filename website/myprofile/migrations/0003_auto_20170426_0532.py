# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-26 05:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myprofile', '0002_auto_20170426_0501'),
    ]

    operations = [
        migrations.AddField(
            model_name='profiles',
            name='importance',
            field=models.IntegerField(default=5),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='skills',
            name='importance',
            field=models.IntegerField(default=5),
            preserve_default=False,
        ),
    ]
