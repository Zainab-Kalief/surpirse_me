
from django.conf.urls import url, include

urlpatterns = [
    url(r'^', include('apps.words_app.urls')),
]
