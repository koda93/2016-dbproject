# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-12-08 21:51
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('notice', '0005_auto_20161209_0633'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='NoticeComment',
            new_name='Comment',
        ),
        migrations.RenameModel(
            old_name='NoticePost',
            new_name='Post',
        ),
    ]