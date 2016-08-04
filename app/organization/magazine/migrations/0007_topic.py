# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-08-04 09:49
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0002_auto_20160725_0143'),
        ('organization-magazine', '0006_auto_20160728_1632'),
    ]

    operations = [
        migrations.CreateModel(
            name='Topic',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='pages.Page')),
                ('articles', models.ManyToManyField(blank=True, to='organization-magazine.Article', verbose_name='articles')),
            ],
            options={
                'verbose_name': 'topic',
                'ordering': ('_order',),
            },
            bases=('pages.page',),
        ),
    ]
