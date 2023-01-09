from django.urls import path
from apps.orders import views

app_name = "apps.orders"

urlpatterns = [
    path("orders", views.UserOrdersView.as_view(), name="info")
]

