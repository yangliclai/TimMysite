# -*- coding:utf-8 -*-
# author:aoaoc
# datetime:7/6/2019 1:39 PM
# software: PyCharm


from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("<int:id>", views.index, name="index"),
    path("create/", views.create, name="create"),
    path("view/", views.view, name="view"),
    # path("<str:name>", views.index, name="index"),
]

