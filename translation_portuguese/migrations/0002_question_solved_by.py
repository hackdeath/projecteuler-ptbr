# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-16 16:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('translation_portuguese', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='solved_by',
            field=models.PositiveSmallIntegerField(default=0),
        ),
    ]