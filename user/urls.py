"""user urls"""


from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^hey/', views.hey, name='hey'),
    url(r'^getUser/', views.getUser, name='getUser'),

]
