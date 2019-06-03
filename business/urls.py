from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^businesses/$', views.businesses, name="businesses"),
    url(r'^business_search/$', views.business_search, name="business_search"),
    url(r'^business/(\d+)', views.business, name="business"),
]