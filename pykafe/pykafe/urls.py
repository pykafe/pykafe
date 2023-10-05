from django.conf import settings
from django.urls import include, path
from django.contrib import admin

from wagtail.admin import urls as wagtailadmin_urls
from wagtail import urls as wagtail_urls
from wagtail.documents import urls as wagtaildocs_urls

from search import views as search_views
from .views import ConsolePython
from django.views.generic import TemplateView


urlpatterns = i18n_patterns(
    # These URLs will have /<language_code>/ appended to the beginning
    path('i18n/', include('django.conf.urls.i18n')),
    path('admin/', include(wagtailadmin_urls)),
    path('django-admin/', admin.site.urls),
    path('documents/', include(wagtaildocs_urls)),
    path('console/', ConsolePython.as_view(), name='console'),
    path('sw.js', TemplateView.as_view(template_name='sw.js', content_type='application/javascript'), name="sw_js"),
    path('search/', search_views.search, name='search'),
    path('', include(wagtail_urls)),
)

if 'rosetta' in settings.INSTALLED_APPS:
    urlpatterns[0:0] += [
        path('rosetta/', include('rosetta.urls'))
    ]
