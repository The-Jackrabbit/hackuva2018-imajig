# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-03-11 20:25
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mainApp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='set',
            name='loser',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='set_loser_id', to='mainApp.User'),
        ),
    ]
