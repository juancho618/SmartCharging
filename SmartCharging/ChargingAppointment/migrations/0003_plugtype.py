# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-12-13 16:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ChargingAppointment', '0002_auto_20161213_1702'),
    ]

    operations = [
        migrations.CreateModel(
            name='PlugType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
    ]
