#-*-  coding:utf-8  -*-
from django.shortcuts import render
from django.contrib.auth.models import User,Group

from rest_framework import permissions,viewsets

from oauth2_provider.ext.rest_framework import TokenHasScope,TokenHasReadWriteScope

from iot.serializers import *
from iot.models import *
from iot.filters import *

# Create your views here.


class RegionMViewSet(viewsets.ModelViewSet):
	#permission_classes = [permissions.IsAuthenticated, TokenHasReadWriteScope]
	queryset=RegionM.objects.all()
	serializer_class=RegionMSerializer


class DevMViewSet(viewsets.ModelViewSet):
	#permission_classes = [permissions.IsAuthenticated, TokenHasReadWriteScope]
	queryset=DevM.objects.all()
	serializer_class=DevMSerializer


class SensorMViewSet(viewsets.ModelViewSet):
	#permission_classes = [permissions.IsAuthenticated, TokenHasReadWriteScope]
	queryset=SensorM.objects.all()
	serializer_class=SensorMSerializer



class DataMViewSet(viewsets.ModelViewSet):
	#permission_classes = [permissions.IsAuthenticated, TokenHasReadWriteScope]
	queryset=DataM.objects.all()
	serializer_class=DataMSerializer
	filter_backends = (filters.DjangoFilterBackend,)
	filter_class = DataMFilter