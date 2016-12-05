"""Organization urls"""
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url('submit_form', views.submit_form, name='submit_form'),
    url(r'^(?P<name>[\w|\D\s]+)/$', views.organization_page, name='organization_page')]
