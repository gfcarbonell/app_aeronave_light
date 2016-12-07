# -*- encoding: utf-8 -*-
from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^aeronave/nuevo/$', views.AeronaveCreateView.as_view(), name='create'),
    url(r'^aeronave/(?P<slug>[-\w\W\d]+)/modificar/$', views.AeronaveUpdateView.as_view(), name='update'),
    url(r'^aeronave/(?P<slug>[-\w\W\d]+)/$', views.AeronaveDetailView.as_view(), name='detail'),

    url(r'^aeronaves/$', views.AeronaveControlListView.as_view(), name='control'),
    url(r'^aeronaves/(?P<search_registro>[-\w\W\d]+)/$', views.AeronaveControlListView.as_view(), name='control'),

]
