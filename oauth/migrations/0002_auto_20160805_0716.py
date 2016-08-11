# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('oauth', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='datam',
            name='sensor',
        ),
        migrations.RemoveField(
            model_name='devm',
            name='region',
        ),
        migrations.RemoveField(
            model_name='sensorm',
            name='dev',
        ),
        migrations.DeleteModel(
            name='DataM',
        ),
        migrations.DeleteModel(
            name='DevM',
        ),
        migrations.DeleteModel(
            name='RegionM',
        ),
        migrations.DeleteModel(
            name='SensorM',
        ),
    ]
