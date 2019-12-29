
from tracking.models import Visitor
from django.utils.translation import ugettext_lazy as _

try:
    from wagtail.core import hooks
    from wagtail.admin.menu import MenuItem
except ImportError:  # fallback for Wagtail <2.0
    from wagtail.wagtailcore import hooks
    from wagtail.wagtailadmin.menu import MenuItem

try:
    from django.urls import reverse
except ImportError:  # fallback for Django <1.9
    from django.core.urlresolvers import reverse

try:
    from django.urls import re_path, include
except ImportError:  # fallback for Django <2.0
    from django.conf.urls import url as re_path
    from django.conf.urls import include

from analytic import urls


@hooks.register('register_admin_urls')
def register_admin_urls():
    return [
        re_path(r'^analytics/', include(urls)),
    ]

@hooks.register('register_admin_urls')
def register_admin_urls():
    return [
        re_path(r'^active-users/', include(urls)),
    ]


@hooks.register('register_admin_menu_item')
def register_styleguide_menu_item():
    return MenuItem(
        _('Analytics'),
        reverse('analytic'),
        classnames='icon icon-fa-bar-chart',
        order=1000
    )


@hooks.register('register_admin_menu_item')
def register_styleguide_menu_item():
    return MenuItem(
        _('Active users'),
        reverse('active_users'),
        classnames='icon icon-user',
        order=1000
    )
