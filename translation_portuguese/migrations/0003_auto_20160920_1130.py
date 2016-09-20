# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-20 14:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('translation_portuguese', '0002_question_solved_by'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='difficulty',
            field=models.PositiveSmallIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='question',
            name='translated',
            field=models.BooleanField(default=False),
        ),
    ]
