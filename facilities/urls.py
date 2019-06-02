from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^facilities/$', views.facilities, name="facilities"),
    url(r'^facility_search/$', views.facility_search, name="facility_search"),
    url(r'^facility_name/(\d+)', views.facility, name="facility"),
]