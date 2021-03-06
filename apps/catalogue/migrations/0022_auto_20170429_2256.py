# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-04-29 17:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalogue', '0021_auto_20170424_2127'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productattributevalue',
            name='value_file',
            field=models.FileField(blank=True, max_length=255, null=True, upload_to='images/products/2017/04/29'),
        ),
        migrations.AlterField(
            model_name='productattributevalue',
            name='value_image',
            field=models.ImageField(blank=True, max_length=255, null=True, upload_to='images/products/2017/04/29'),
        ),
        migrations.AlterField(
            model_name='productimage',
            name='original',
            field=models.ImageField(max_length=255, upload_to='images/products/2017/04/29', verbose_name='Original'),
        ),
    ]
