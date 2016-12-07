# -*- encoding: utf-8 -*-
from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^piloto/nuevo/$', views.PilotoCreateView.as_view(), name='create'),
    url(r'^piloto/(?P<slug>[-\w\W\d]+)/modificar/$', views.PilotoUpdateView.as_view(), name='update'),
    url(r'^pilotos/$', views.PilotoControlListView.as_view(), name='control'),
    url(r'^pilotos/(?P<search_registro>[-\w\W\d]+)/$', views.PilotoControlListView.as_view(), name='control'),
    url(r'^piloto/(?P<slug>[-\w\W\d]+)/$', views.PilotoDetailView.as_view(), name='detail'),

]
