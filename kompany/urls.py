from django.conf.urls import url
from kompany import views

urlpatterns = [
    url(r'^$', views.home_page),
    url(r'^(?P<name>[-\w]+)/$', views.laptop_details, name='laptop_details'),
]
