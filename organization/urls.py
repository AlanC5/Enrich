"""Organization urls"""
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<name>[\w|\D\s]+)/$', views.organization_page, name='organization_page')]
