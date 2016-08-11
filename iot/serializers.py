#-*- coding: utf-8 -*-
from rest_framework import  serializers
from django.contrib.auth.models import User,Group
from iot.models import *


class DevMSerializer(serializers.ModelSerializer):
	class Meta:
		model=DevM


class RegionMSerializer(serializers.ModelSerializer):
	class Meta:
		model=RegionM


class SensorMSerializer(serializers.ModelSerializer):
	class Meta:
		model=SensorM

class DataMSerializer(serializers.ModelSerializer):
	class Meta:
		model=DataM
		fields = ('sensor','data','date_time')