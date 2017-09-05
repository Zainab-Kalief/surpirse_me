from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.index),
    url(r'^proccess$', views.surprise),
    url(r'^results$', views.result),
]
