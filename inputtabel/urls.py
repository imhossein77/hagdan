from django.urls import path
from . import views

app_name = "input"

urlpatterns = [
    path('', views.input, name="inputtabel"),
    # path("", views.Prouduct_list, name="innnnn")
]