# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-01-01 12:34
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0004_auto_20171230_1458'),
    ]

    operations = [
        migrations.RenameField(
            model_name='buyingproduct',
            old_name='product_id',
            new_name='product',
        ),
    ]