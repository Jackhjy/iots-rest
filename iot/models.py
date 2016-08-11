#-*- coding:utf-8 -*-
from django.contrib import admin
from django.db import models
from django.utils import timezone
# Create your models here.

# Create your models here.
#Define region model
class  RegionM(models.Model):
	region_id = models.PositiveIntegerField(unique = True,verbose_name=(u"区域编号"))
	region_info = models.CharField(max_length=50,blank=True,verbose_name=(u'区域描述'))
	region_name = models.CharField(max_length=50,blank=True,verbose_name=(u'区域名称'))
	reserved = models.CharField(max_length=100,blank=True,verbose_name=(u'保留项1'))
	reserved2 = models.CharField(max_length=100,blank=True,verbose_name=(u'保留项2'))
	access_key = models.CharField(max_length=32,blank=True,verbose_name=(u'访问Key'))
	date_time = models.DateTimeField(default=timezone.now,verbose_name=(u'修改时间'))
	region_position=models.CharField(max_length=100,blank=True,verbose_name=(u'GPS坐标'))
	enable=models.BooleanField(default=False,verbose_name=(u'区域使能位'))
	def __unicode__(self):
		return str(self.region_id)


class DevM(models.Model):
	dev_id = models.PositiveIntegerField(unique = True,verbose_name=(u'设备编号'))
	dev_info = models.CharField(max_length= 200,blank=True,verbose_name=(u'设备描述'))
	region  = models.ForeignKey(RegionM,verbose_name=(u'所属区域'))
	dev_name = models.CharField(max_length=50,blank=True,verbose_name=(u'设备名称'))
	access_key = models.CharField(max_length=32,blank=True,verbose_name=(u'访问Key'))
	dev_sn	=  models.CharField(max_length=48,blank=True,verbose_name=(u'设备序列号'))
	date_time = models.DateTimeField(default=timezone.now,verbose_name=(u'修改时间'))
	dev_position=models.CharField(max_length=100,blank=True,verbose_name=(u'GPS坐标'))
	enable=models.BooleanField(default=False,verbose_name=(u'设备使能位'))
	reserved = models.CharField(max_length=100,blank=True,verbose_name=(u'保留项1'))
	reserved2 = models.CharField(max_length=100,blank=True,verbose_name=(u'保留项2'))
	def __unicode__(self):
		return str(self.dev_id)


SENSOR_TYPE=(
		('A',u'电流'),
		('V',u'电压'),
		('T',u'温度'),
		('H',u'湿度'),
		('P',u'压力'),
		('L',u'位置'),
		('Y',u'时间'),
		('F',u'文件'),
		('I',u'消息'),
		('J',u'图片'),
	)
SENSOR_SYMBOL=(
		(u'A',u'安培'),
		(u'kA',u'千安培'),
		(u'V',u'伏特'),
		(u'kV',u'千伏特'),
		(u'℃',u'摄氏度'),
		(u'%',u'百分数'),
		(u'MPa',u'兆帕'),
		(u'kPa',u'千帕'),
		(u'Pa',u'帕'),
		(u'经纬度',u'经纬度'),
		(' ',u'无'),
	)
class SensorM(models.Model):
	sensor_id = models.PositiveIntegerField(unique = True,verbose_name=(u'传感器编号'))
	sensor_info = models.CharField(max_length=200,blank=True,verbose_name=(u'传感器描述'))
	dev = models.ForeignKey(DevM,verbose_name=(u'传感器所属设备'))
	sensor_type = models.CharField(max_length = 10,choices=SENSOR_TYPE,verbose_name=(u'传感器类型'))
	sensor_name = models.CharField(max_length=50,blank=True,verbose_name=(u'传感器名称'))
	date_time = models.DateTimeField(default=timezone.now,verbose_name=(u'修改时间'))
	sensor_position=models.CharField(max_length=100,blank=True,verbose_name=(u'GPS坐标'))
	enable=models.BooleanField(default=False,verbose_name=(u'传感器使能位'))
	data_scale = models.FloatField(verbose_name=(u'数据标度'))
	data_symbol=models.CharField(max_length=20,choices=SENSOR_SYMBOL,verbose_name=(u'数据符号'))
	top_limit=models.FloatField(verbose_name=(u'测量上限'),default=100.0)
	down_limit= models.FloatField(verbose_name=(u'测量下限'),default=0.0)
	reserved = models.CharField(max_length=100,blank=True,verbose_name=(u'保留项1'))
	reserved2 = models.CharField(max_length=100,blank=True,verbose_name=(u'保留项2'))
	def __unicode__(self):
		return str(self.sensor_id)


class DataM(models.Model):
	date_time = models.DateTimeField(default=timezone.now,verbose_name=(u'采集时间'))
	data = models.FloatField(verbose_name=(u'数据'))
	sensor  = models.ForeignKey(SensorM,verbose_name=(u'数据所属设备'))

