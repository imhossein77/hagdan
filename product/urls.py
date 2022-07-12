from django.urls import path
from . import views

app_name = "product"

urlpatterns = [
    path('', views.Prouduct_list, name="products"),
    path("<int:id>/", views.Product_detail, name="product"),
    path("category/<slug:category>", views.prouduct, name="product_category"),
]
