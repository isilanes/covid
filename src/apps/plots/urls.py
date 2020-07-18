from django.urls import path

from . import views


app_name = "plots"


urlpatterns = [
    path('', views.main, name="main"),
]
