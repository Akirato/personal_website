# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-26 06:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myprofile', '0008_auto_20170426_0655'),
    ]

    operations = [
        migrations.AddField(
            model_name='projects',
            name='link',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
