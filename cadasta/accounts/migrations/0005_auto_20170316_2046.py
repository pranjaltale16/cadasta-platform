# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-03-16 20:46
from __future__ import unicode_literals

import buckets.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_auto_20170316_1143'),
    ]

    operations = [
        migrations.AlterField(
            model_name='historicaluser',
            name='file',
            field=buckets.fields.S3FileField(blank=True, upload_to='users'),
        ),
        migrations.AlterField(
            model_name='user',
            name='file',
            field=buckets.fields.S3FileField(blank=True, upload_to='users'),
        ),
    ]