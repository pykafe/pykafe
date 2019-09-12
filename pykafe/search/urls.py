
from django.conf.urls import include, url
from .views import dashboard

urlpatterns = [
    url(r'^analytic/$', dashboard, name='analytic'),
]
