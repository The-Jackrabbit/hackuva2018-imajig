# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-03-22 01:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainApp', '0003_user_bio'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='icon_url',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
    ]
