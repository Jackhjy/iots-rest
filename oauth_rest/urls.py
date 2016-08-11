"""oauth_rest URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import patterns, url, include
from django.contrib import admin
from rest_framework.routers import DefaultRouter
import oauth.views
import iot.views


router = DefaultRouter()
router.register(r'users', oauth.views.UserViewSet)
router.register(r'groups', oauth.views.GroupViewSet)
router.register(r'regions',iot.views.RegionMViewSet)
router.register(r'devs',iot.views.DevMViewSet)
router.register(r'sensors',iot.views.SensorMViewSet)
router.register(r'datas',iot.views.DataMViewSet)

urlpatterns = patterns('',
    url(r'^', include(router.urls)),
    url(r'^o/', include('oauth2_provider.urls', namespace='oauth2_provider')),
    url(r'^admin/', include(admin.site.urls))
)
