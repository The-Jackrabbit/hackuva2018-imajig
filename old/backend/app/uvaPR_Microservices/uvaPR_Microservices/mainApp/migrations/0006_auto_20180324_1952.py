# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-03-24 19:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainApp', '0005_fileupload'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fileupload',
            name='datafile',
            field=models.ImageField(blank=True, null=True, upload_to='media/users/'),
        ),
    ]