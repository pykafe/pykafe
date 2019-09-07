
from wagtail.contrib.modeladmin.options import (
    ModelAdmin,
    ModelAdminGroup,
    modeladmin_register
)
from tracking.models import Visitor, Pageview
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

from search import urls


@hooks.register('register_admin_urls')
def register_admin_urls():
    return [
        re_path(r'^analytics/', include(urls)),
    ]


@hooks.register('register_rich_text_features')
def make_h1_default(features):
    features.default_features.append('h1')


class VisitorAdmin(ModelAdmin):
    model = Visitor
    menu_label = "Visitor"
    menu_icon = "pick"
    menu_order = 300
    add_to_settings_menu = False
    exclude_from_explorer = False
    list_display = ('session_key', 'user', 'start_time', 'ip_address', 'user_agent')
    list_filter = ('user', 'ip_address')
    search_fields = ('user',)


class PageviewAdmin(ModelAdmin):
    model = Pageview
    menu_label = "PageView"
    menu_icon = "pilcrow"
    menu_order = 200
    add_to_settings_menu = False
    exclude_from_explorer = False
    list_display = ('url', 'view_time')
    list_filter = ('url', 'view_time')
    search_fields = ('url',)


@hooks.register('register_admin_menu_item')
def register_styleguide_menu_item():
    return MenuItem(
        _('Analytics'),
        reverse('tracking'),
        classnames='icon icon-fa-bar-chart',
        order=1000
    )


#class VisitorGroup(ModelAdminGroup):
    #menu_label = "Visitors"
    #menu_icon = "pick"
    #menu_order = 500
    #items = (VisitorAdmin, PageviewAdmin)


modeladmin_register(VisitorAdmin)
modeladmin_register(PageviewAdmin)
#modeladmin_register(VisitorGroup)
