
from django.urls import include, path
from .views import dashboard, active_users_info_view


urlpatterns = [
    path('active-users/', active_users_info_view, name="active_users"),
    path('analytic/', dashboard, name='analytic'),
]
