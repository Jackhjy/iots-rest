#-*- coding: utf-8 -*-
from rest_framework import  serializers
from django.contrib.auth.models import User,Group
from oauth.models import *

class UserSerializer(serializers.ModelSerializer):
	class Meta:
		model=User

class GroupSerializer(serializers.ModelSerializer):
	class Meta:
		model=Group
