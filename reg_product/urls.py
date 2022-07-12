from django.urls import path
from . import views

app_name = "register_product"

urlpatterns = [
    path('', views.reg_product, name="register_product")
]
