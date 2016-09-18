from django.conf.urls import url
from .                 import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^problemas$', views.archives, name='archives'),
    url(r'^problemas/(?P<pagina>\d+)$', views.archives, name='archives'),
    url(r'^problema/(?P<id>\d+)$', views.problem, name='problem'),
]
