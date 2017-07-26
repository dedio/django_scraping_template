# -*- coding: utf-8 -*-

from django.conf.urls import include, url
from . import views

urlpatterns = [
        url(r'^cliente01/', views.cliente01),
    ]
