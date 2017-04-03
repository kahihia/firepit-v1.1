# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-03 18:04
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('address', '0002_address'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='address',
            name='country',
        ),
        migrations.AlterField(
            model_name='useraddress',
            name='country',
            field=models.ForeignKey(default='India', on_delete=django.db.models.deletion.CASCADE, to='address.Country', verbose_name='Country'),
        ),
        migrations.DeleteModel(
            name='Address',
        ),
    ]
