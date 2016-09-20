from django.conf.urls import url
from .                 import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^problemas$', views.archives, name='archives_empty'),
    url(r'^problemas/(?P<page>\d+)$', views.archives, name='archives'),
    url(r'^problema$', views.problem, name='problem_empty'),
    url(r'^problema/(?P<id>\d+)$', views.problem, name='problem'),
    url(r'^recentes$', views.recents, name='recents'),
]
