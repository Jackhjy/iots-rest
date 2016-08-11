#-*-  coding:utf-8  -*-
from django.shortcuts import render
from django.contrib.auth.models import User,Group

from rest_framework import permissions,viewsets

from oauth2_provider.ext.rest_framework import TokenHasScope,TokenHasReadWriteScope

from oauth.serializers import *
from oauth.models import *

# Create your views here.

class UserViewSet(viewsets.ModelViewSet):
	#permission_classes = [permissions.IsAuthenticated, TokenHasReadWriteScope]
	queryset=User.objects.all()
	serializer_class=UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
	permission_classes = [permissions.IsAuthenticated, TokenHasScope]
	required_scopes=['groups']
	queryset=Group.objects.all()
	serializer_class=GroupSerializer

