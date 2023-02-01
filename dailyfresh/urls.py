"""dailyfresh URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include
from django.urls import path, re_path
from django.contrib import admin
from django.views.generic import RedirectView

urlpatterns = [
    re_path(r"^/?$", RedirectView.as_view(url="/goods/index")),
    path(r'admin/', admin.site.urls),
    # url(r'^.*$', TemplateView.as_view(template_name="static_ok_index.html")),  # 用户模块
    re_path(r'^users/', include('apps.users.urls', namespace='users')),  # 用户模块
    re_path(r'^goods/', include('apps.goods.urls', namespace='goods')),  # 商品模块
    re_path(r'^cart/', include('apps.cart.urls', namespace='cart')),  # 购物车模块
    re_path(r'^orders/', include('apps.orders.urls', namespace='orders')),  # 订单模块
]
