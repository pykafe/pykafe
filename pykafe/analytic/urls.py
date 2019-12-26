
from django.urls import include, path
from .views import dashboard

urlpatterns = [
    path('analytic/', dashboard, name='analytic'),
]
