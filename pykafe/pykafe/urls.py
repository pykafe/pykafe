from django.conf import settings
from django.urls import include, path
from django.contrib import admin

from wagtail.admin import urls as wagtailadmin_urls
from wagtail.core import urls as wagtail_urls
from wagtail.documents import urls as wagtaildocs_urls
from django.conf.urls.i18n import i18n_patterns

from search import views as search_views
from .views import KonversaView
from django.views.generic import TemplateView


urlpatterns = [
    path('pykafe-admin/', admin.site.urls),
    path('admin/', include(wagtailadmin_urls)),
    path('documents/', include(wagtaildocs_urls)),
]

urlpatterns += i18n_patterns(
    # These URLs will have /<language_code>/ appended to the beginning
    path('i18n/', include('django.conf.urls.i18n')),
    path('konversa/', KonversaView.as_view(), name='konversa'),
    path('sw.js', TemplateView.as_view(template_name='sw.js', content_type='application/javascript'), name="sw_js"),
    path('search/', search_views.search, name='search'),
    path('', include(wagtail_urls)),
)

if 'rosetta' in settings.INSTALLED_APPS:
    urlpatterns[0:0] += [
        path('rosetta/', include('rosetta.urls'))
    ]

if settings.DEBUG:
    from django.conf.urls.static import static
    from django.contrib.staticfiles.urls import staticfiles_urlpatterns

    # Serve static and media files from development server
    urlpatterns += staticfiles_urlpatterns()
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
