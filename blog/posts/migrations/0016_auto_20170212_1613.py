# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-12 12:13
from __future__ import unicode_literals

from django.db import migrations, models
import posts.models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0015_attachment'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='post_image',
        ),
        migrations.AddField(
            model_name='post',
            name='files',
            field=models.ManyToManyField(blank=True, null=True, related_name='files', to='posts.Attachment'),
        ),
        migrations.AlterField(
            model_name='attachment',
            name='attachment',
            field=models.FileField(upload_to=posts.models.upload_location),
        ),
    ]