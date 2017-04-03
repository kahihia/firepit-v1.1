# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-09 18:40
from __future__ import unicode_literals

from django.db import migrations, models
import firepit.models


class Migration(migrations.Migration):

    dependencies = [
        ('firepit', '0003_requestquote_requestquoteimage'),
    ]

    operations = [
        migrations.AlterField(
            model_name='requestquoteimage',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=firepit.models.get_quote_image_name, verbose_name='Image'),
        ),
    ]