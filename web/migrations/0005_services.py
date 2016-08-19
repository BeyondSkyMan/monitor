# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-21 15:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0004_graphs'),
    ]

    operations = [
        migrations.CreateModel(
            name='Services',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True)),
                ('monitor_type', models.CharField(choices=[(b'agent', b'Agent'), (b'snmp', b'SNMP'), (b'wget', b'Wget')], max_length=50)),
                ('plugin', models.CharField(max_length=100)),
                ('item_list', models.ManyToManyField(to='web.Items')),
            ],
        ),
    ]
