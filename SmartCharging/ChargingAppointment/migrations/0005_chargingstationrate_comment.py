# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-12-18 11:59
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('ChargingAppointment', '0004_chargingstationrate'),
    ]

    operations = [
        migrations.AddField(
            model_name='chargingstationrate',
            name='comment',
            field=models.CharField(default=django.utils.timezone.now, max_length=255),
            preserve_default=False,
        ),
    ]