# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-04-29 17:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('firepit', '0012_homesolution_order_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='homesolution',
            name='background_image',
            field=models.ImageField(null=True, upload_to='home_solutions/background'),
        ),
    ]
