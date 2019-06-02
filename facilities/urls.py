from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^facilities/$', views.facilities, name="facilities"),
    url(r'^facilit_search/$', views.facility_search, name="facility_search"),
]