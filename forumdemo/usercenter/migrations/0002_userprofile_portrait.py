# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-09-26 08:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usercenter', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='portrait',
            field=models.CharField(blank=True, max_length=300, verbose_name='头像'),
        ),
    ]
