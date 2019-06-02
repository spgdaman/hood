from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^businesses/$', views.businesses, name="businesses"),
]