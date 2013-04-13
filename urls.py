from django.conf.urls import patterns, include, url
from django_bingo import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
)
