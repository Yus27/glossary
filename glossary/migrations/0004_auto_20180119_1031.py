# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2018-01-19 01:31
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('glossary', '0003_auto_20180118_1349'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pair',
            name='comments',
        ),
        migrations.RemoveField(
            model_name='pair',
            name='source',
        ),
        migrations.RemoveField(
            model_name='pair',
            name='tags',
        ),
        migrations.DeleteModel(
            name='Source',
        ),
        migrations.DeleteModel(
            name='Tag',
        ),
    ]
