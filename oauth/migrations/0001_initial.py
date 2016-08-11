# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DataM',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date_time', models.DateTimeField(default=django.utils.timezone.now, verbose_name='\u91c7\u96c6\u65f6\u95f4')),
                ('data', models.FloatField(verbose_name='\u6570\u636e')),
            ],
        ),
        migrations.CreateModel(
            name='DevM',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('dev_id', models.PositiveIntegerField(unique=True, verbose_name='\u8bbe\u5907\u7f16\u53f7')),
                ('dev_info', models.CharField(max_length=200, verbose_name='\u8bbe\u5907\u63cf\u8ff0', blank=True)),
                ('dev_name', models.CharField(max_length=50, verbose_name='\u8bbe\u5907\u540d\u79f0', blank=True)),
                ('access_key', models.CharField(max_length=32, verbose_name='\u8bbf\u95eeKey', blank=True)),
                ('dev_sn', models.CharField(max_length=48, verbose_name='\u8bbe\u5907\u5e8f\u5217\u53f7', blank=True)),
                ('date_time', models.DateTimeField(default=django.utils.timezone.now, verbose_name='\u4fee\u6539\u65f6\u95f4')),
                ('dev_position', models.CharField(max_length=100, verbose_name='GPS\u5750\u6807', blank=True)),
                ('enable', models.BooleanField(default=False, verbose_name='\u8bbe\u5907\u4f7f\u80fd\u4f4d')),
                ('reserved', models.CharField(max_length=100, verbose_name='\u4fdd\u7559\u98791', blank=True)),
                ('reserved2', models.CharField(max_length=100, verbose_name='\u4fdd\u7559\u98792', blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='RegionM',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('region_id', models.PositiveIntegerField(unique=True, verbose_name='\u533a\u57df\u7f16\u53f7')),
                ('region_info', models.CharField(max_length=50, verbose_name='\u533a\u57df\u63cf\u8ff0', blank=True)),
                ('region_name', models.CharField(max_length=50, verbose_name='\u533a\u57df\u540d\u79f0', blank=True)),
                ('reserved', models.CharField(max_length=100, verbose_name='\u4fdd\u7559\u98791', blank=True)),
                ('reserved2', models.CharField(max_length=100, verbose_name='\u4fdd\u7559\u98792', blank=True)),
                ('access_key', models.CharField(max_length=32, verbose_name='\u8bbf\u95eeKey', blank=True)),
                ('date_time', models.DateTimeField(default=django.utils.timezone.now, verbose_name='\u4fee\u6539\u65f6\u95f4')),
                ('region_position', models.CharField(max_length=100, verbose_name='GPS\u5750\u6807', blank=True)),
                ('enable', models.BooleanField(default=False, verbose_name='\u533a\u57df\u4f7f\u80fd\u4f4d')),
            ],
        ),
        migrations.CreateModel(
            name='SensorM',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('sensor_id', models.PositiveIntegerField(unique=True, verbose_name='\u4f20\u611f\u5668\u7f16\u53f7')),
                ('sensor_info', models.CharField(max_length=200, verbose_name='\u4f20\u611f\u5668\u63cf\u8ff0', blank=True)),
                ('sensor_type', models.CharField(max_length=10, verbose_name='\u4f20\u611f\u5668\u7c7b\u578b', choices=[(b'A', '\u7535\u6d41'), (b'V', '\u7535\u538b'), (b'T', '\u6e29\u5ea6'), (b'H', '\u6e7f\u5ea6'), (b'P', '\u538b\u529b'), (b'L', '\u4f4d\u7f6e'), (b'Y', '\u65f6\u95f4'), (b'F', '\u6587\u4ef6'), (b'I', '\u6d88\u606f'), (b'J', '\u56fe\u7247')])),
                ('sensor_name', models.CharField(max_length=50, verbose_name='\u4f20\u611f\u5668\u540d\u79f0', blank=True)),
                ('date_time', models.DateTimeField(default=django.utils.timezone.now, verbose_name='\u4fee\u6539\u65f6\u95f4')),
                ('sensor_position', models.CharField(max_length=100, verbose_name='GPS\u5750\u6807', blank=True)),
                ('enable', models.BooleanField(default=False, verbose_name='\u4f20\u611f\u5668\u4f7f\u80fd\u4f4d')),
                ('data_scale', models.FloatField(verbose_name='\u6570\u636e\u6807\u5ea6')),
                ('data_symbol', models.CharField(max_length=20, verbose_name='\u6570\u636e\u7b26\u53f7', choices=[('A', '\u5b89\u57f9'), ('kA', '\u5343\u5b89\u57f9'), ('V', '\u4f0f\u7279'), ('kV', '\u5343\u4f0f\u7279'), ('\u2103', '\u6444\u6c0f\u5ea6'), ('%', '\u767e\u5206\u6570'), ('MPa', '\u5146\u5e15'), ('kPa', '\u5343\u5e15'), ('Pa', '\u5e15'), ('\u7ecf\u7eac\u5ea6', '\u7ecf\u7eac\u5ea6'), (b' ', '\u65e0')])),
                ('top_limit', models.FloatField(default=100.0, verbose_name='\u6d4b\u91cf\u4e0a\u9650')),
                ('down_limit', models.FloatField(default=0.0, verbose_name='\u6d4b\u91cf\u4e0b\u9650')),
                ('reserved', models.CharField(max_length=100, verbose_name='\u4fdd\u7559\u98791', blank=True)),
                ('reserved2', models.CharField(max_length=100, verbose_name='\u4fdd\u7559\u98792', blank=True)),
                ('dev', models.ForeignKey(verbose_name='\u4f20\u611f\u5668\u6240\u5c5e\u8bbe\u5907', to='oauth.DevM')),
            ],
        ),
        migrations.AddField(
            model_name='devm',
            name='region',
            field=models.ForeignKey(verbose_name='\u6240\u5c5e\u533a\u57df', to='oauth.RegionM'),
        ),
        migrations.AddField(
            model_name='datam',
            name='sensor',
            field=models.ForeignKey(verbose_name='\u6570\u636e\u6240\u5c5e\u8bbe\u5907', to='oauth.SensorM'),
        ),
    ]
