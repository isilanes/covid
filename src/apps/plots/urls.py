from django.urls import path

from . import views


app_name = "plots"


urlpatterns = [
    path('', views.show, name="show"),
    path('insert', views.insert, name="insert"),
]
