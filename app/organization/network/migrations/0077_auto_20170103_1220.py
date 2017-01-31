# -*- coding: utf-8 -*-
# Generated by Django 1.9.11 on 2017-01-03 11:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('organization-network', '0076_auto_20161230_1839'),
    ]

    operations = [
        migrations.AddField(
            model_name='organizationblock',
            name='login_required',
            field=models.BooleanField(default=False, verbose_name='login required'),
        ),
        migrations.AddField(
            model_name='personblock',
            name='login_required',
            field=models.BooleanField(default=False, verbose_name='login required'),
        ),
    ]