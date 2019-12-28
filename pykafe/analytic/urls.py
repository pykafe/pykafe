
from django.conf.urls import include, url
from django.urls import include, path
from .views import dashboard, active_users_info_view


urlpatterns = [
    path('active-users/', active_users_info_view, name="active_users"),
    path(r'analytic/', dashboard, name='analytic'),
]
