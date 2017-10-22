from django.conf.urls import url
from kompany import views

urlpatterns = [
    url(r'^$', views.home_page, name='home'),
    url(r'^(?P<category>[-\w]+)/$', views.category_view, name='product_list'),
]
