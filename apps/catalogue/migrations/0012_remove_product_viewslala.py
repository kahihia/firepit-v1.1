# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-03 17:24
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalogue', '0011_auto_20170303_2246'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='viewslala',
        ),
    ]