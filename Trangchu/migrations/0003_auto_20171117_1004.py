# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-17 03:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Trangchu', '0002_sanpham'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sanpham',
            name='Caukien',
            field=models.TextField(null=True),
        ),
    ]