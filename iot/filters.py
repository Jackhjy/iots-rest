#-*- coding: utf-8 -*-
import django_filters
from iot.models import  *
from rest_framework import filters


class  DataMFilter(filters.FilterSet):
	data = django_filters.RangeFilter()
	start_time = django_filters.DateTimeFilter(name='date_time',lookup_expr='gte')
	end_time =  django_filters.DateTimeFilter(name='date_time',lookup_expr='lte')
	sensor = django_filters.NumberFilter(name='sensor__id')
	class Meta:
		model = DataM
		fields = ['start_time','end_time','data','sensor']
