#!/usr/bin/python
# -*- coding:utf-8 -*-

from django.urls import path, re_path
from apps.users import views

app_name = "apps.users"


urlpatterns = [
    re_path(r'^register$', views.RegisterView.as_view(), name='register'),  # 注册视图
    re_path(r'^login$', views.LoginView.as_view(), name='login'),  # 登入视图
    re_path(r'^logout$', views.LogoutView.as_view(), name='logout'),  # 登入视图
    re_path(r'^activate/(?P<token>.+)$', views.ActivateView.as_view(), name='activate'),  # 激活用户视图
    re_path(r'^address$', views.AddressView.as_view(), name='address'),  # 个人中心收货地址
    re_path(r'^userinfo$', views.UserinfoView.as_view(), name='info'),  # 个人中心收货地址
]



