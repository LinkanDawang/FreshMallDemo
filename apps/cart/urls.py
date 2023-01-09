# from django.conf.urls import url
from django.urls import re_path
from cart import views

app_name = "apps.cart"

urlpatterns = [
    re_path(r'^add$', views.AddCartView.as_view(), name='add'),  # 添加商品到购物车
    re_path(r'^$', views.CartInfoView.as_view(), name='info'),  # 购物车页面
    re_path(r'^update$', views.UpdateCartView.as_view(), name='update'),  # 修改商品数量
    re_path(r'^delete', views.DeleteCartView.as_view(), name='delete'),  # 删除购物车的商品
]
