# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-10 11:10
from __future__ import unicode_literals

from django.db import migrations, models
import posts.models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0011_auto_20170210_0831'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='post_image',
            field=models.FileField(blank=True, null=True, upload_to=posts.models.upload_location),
        ),
    ]
