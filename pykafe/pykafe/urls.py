from django.conf import settings
from django.conf.urls import include, url
from django.contrib import admin

from wagtail.admin import urls as wagtailadmin_urls
from wagtail.core import urls as wagtail_urls
from wagtail.documents import urls as wagtaildocs_urls
from django.conf.urls.i18n import i18n_patterns

from search import views as search_views
from .views import KonversaView, ConsolePython


urlpatterns = [
    url(r'^django-admin/', admin.site.urls),
    url(r'^admin/', include(wagtailadmin_urls)),
    url(r'^documents/', include(wagtaildocs_urls)),
]

urlpatterns += i18n_patterns(
    # These URLs will have /<language_code>/ appended to the beginning
    url('i18n/', include('django.conf.urls.i18n')),
    url(r'konversa/', KonversaView.as_view(), name='konversa'),
    url(r'console/', ConsolePython.as_view(), name='console'),
    url(r'^search/$', search_views.search, name='search'),
    url(r'', include(wagtail_urls)),
)

if 'rosetta' in settings.INSTALLED_APPS:
    urlpatterns[0:0] += [
        url(r'^rosetta/', include('rosetta.urls'))
    ]

if settings.DEBUG:
    from django.conf.urls.static import static
    from django.contrib.staticfiles.urls import staticfiles_urlpatterns

    # Serve static and media files from development server
    urlpatterns += staticfiles_urlpatterns()
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
