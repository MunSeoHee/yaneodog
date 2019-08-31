from django.urls import path
from . import views
from django.conf.urls import url

urlpatterns = [
    path('', views.compare, name="compare"),
    url(r'^data.json$', views.data_json),
]
