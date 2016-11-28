# Create your urls here.
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, o_name='index'),
    url(r'^(?P<name>)/$', views.organization_page, o_name='organization_page')]
