from django.urls import path
from django.conf.urls import url
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('list', views.list),
    path('new', views.new),

    # /products/id
    url(r'^(?P<album_id>[0-9]+)/$', views.detail, name='detail'),
]
