from django.conf.urls import url
from . import views

urlpatterns=[
    url(r'^index/$', views.home, name='home'),
    url(r'^new/hood$', views.new_hood, name='new_hood')
]