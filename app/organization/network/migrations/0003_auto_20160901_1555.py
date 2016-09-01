# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-09-01 13:55
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sites', '0002_alter_domain_unique'),
        ('organization-network', '0002_auto_20160824_0020'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='organization',
            name='custommodel_ptr',
        ),
        migrations.RemoveField(
            model_name='person',
            name='customdisplayable_ptr',
        ),
        migrations.AddField(
            model_name='organization',
            name='id',
            field=models.AutoField(auto_created=True, default=1, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='person',
            name='_meta_title',
            field=models.CharField(blank=True, help_text='Optional title to be used in the HTML title tag. If left blank, the main title field will be used.', max_length=500, null=True, verbose_name='Title'),
        ),
        migrations.AddField(
            model_name='person',
            name='created',
            field=models.DateTimeField(editable=False, null=True),
        ),
        migrations.AddField(
            model_name='person',
            name='description',
            field=models.TextField(blank=True, verbose_name='Description'),
        ),
        migrations.AddField(
            model_name='person',
            name='expiry_date',
            field=models.DateTimeField(blank=True, help_text="With Published chosen, won't be shown after this time", null=True, verbose_name='Expires on'),
        ),
        migrations.AddField(
            model_name='person',
            name='gen_description',
            field=models.BooleanField(default=True, help_text='If checked, the description will be automatically generated from content. Uncheck if you want to manually set a custom description.', verbose_name='Generate description'),
        ),
        migrations.AddField(
            model_name='person',
            name='id',
            field=models.AutoField(auto_created=True, default=1, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='person',
            name='in_sitemap',
            field=models.BooleanField(default=True, verbose_name='Show in sitemap'),
        ),
        migrations.AddField(
            model_name='person',
            name='keywords_string',
            field=models.CharField(blank=True, editable=False, max_length=500),
        ),
        migrations.AddField(
            model_name='person',
            name='publish_date',
            field=models.DateTimeField(blank=True, db_index=True, help_text="With Published chosen, won't be shown until this time", null=True, verbose_name='Published from'),
        ),
        migrations.AddField(
            model_name='person',
            name='short_url',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='person',
            name='site',
            field=models.ForeignKey(default=1, editable=False, on_delete=django.db.models.deletion.CASCADE, to='sites.Site'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='person',
            name='slug',
            field=models.CharField(blank=True, help_text='Leave blank to have the URL auto-generated from the title.', max_length=2000, null=True, verbose_name='URL'),
        ),
        migrations.AddField(
            model_name='person',
            name='status',
            field=models.IntegerField(choices=[(1, 'Draft'), (2, 'Published')], default=2, help_text='With Draft chosen, will only be shown for admin users on the site.', verbose_name='Status'),
        ),
        migrations.AddField(
            model_name='person',
            name='title',
            field=models.CharField(default='a', max_length=500, verbose_name='Title'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='person',
            name='updated',
            field=models.DateTimeField(editable=False, null=True),
        ),
    ]
