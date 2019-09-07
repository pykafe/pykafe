
from django.conf.urls import include, url
from .views import dashboard

urlpatterns = [
    url(r'^anality/$', dashboard, name='tracking'),
]
