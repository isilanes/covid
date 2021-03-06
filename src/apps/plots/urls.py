from django.urls import path

from . import views, api


app_name = "plots"


urlpatterns = [
    # Views:
    path('', views.show, name="show"),
    path('insert', views.insert, name="insert"),

    # API:
    path('get_country_data', api.get_country_data, name="get_country_data"),
]
