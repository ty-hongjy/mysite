# -*- coding: utf-8 -*-
from django.urls import path
from . import views

urlpatterns=[
    path('hello/',views.hello),
    path('hello1/',views.hello1)
#    path('',views.hello1)
    ]