# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-09-14 16:18
from __future__ import unicode_literals

from django.db import migrations
import mezzanine.core.fields


class Migration(migrations.Migration):

    dependencies = [
        ('organization-core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='linktype',
            name='picto',
            field=mezzanine.core.fields.FileField(default='', max_length=1024, verbose_name='picto'),
            preserve_default=False,
        ),
    ]