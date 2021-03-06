# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-25 19:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='achievements',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('achievement', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='cocurricular',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('activity', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='education',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('degree', models.CharField(max_length=100)),
                ('year_started', models.CharField(max_length=10)),
                ('year_ended', models.CharField(max_length=10)),
                ('institute', models.CharField(max_length=100)),
                ('cgpa', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='profileinfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
                ('address', models.CharField(max_length=40)),
                ('email', models.EmailField(max_length=255, unique=True, verbose_name='email address')),
                ('contact_number', models.CharField(max_length=13)),
                ('description', models.CharField(max_length=300)),
                ('degree', models.CharField(max_length=100)),
                ('college', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='profiles',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10)),
                ('profile_name', models.CharField(max_length=30)),
                ('link', models.CharField(max_length=200)),
                ('types', models.CharField(blank=True, choices=[('Misc', 'Misc'), ('Research', 'Research'), ('Developer', 'Developer')], default='Developer', max_length=6, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='projects',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('importance', models.IntegerField()),
                ('start_date', models.CharField(max_length=10)),
                ('end_date', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='publications',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('headline', models.CharField(max_length=100)),
                ('conference', models.CharField(max_length=100)),
                ('link', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='skills',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('proficiency', models.IntegerField()),
                ('types', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='work_experience',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('position', models.CharField(max_length=50)),
                ('company', models.CharField(max_length=100)),
                ('start', models.CharField(max_length=10)),
                ('description', models.CharField(max_length=10)),
                ('link', models.CharField(max_length=200)),
            ],
        ),
    ]
