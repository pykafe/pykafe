from django.contrib.staticfiles.templatetags.staticfiles import static
from django.utils.html import format_html

try:
    from wagtail.core import hooks
except ImportError:  # fallback for Wagtail <2.0
    from wagtail.wagtailcore import hooks


@hooks.register('register_rich_text_features')
def make_h1_default(features):
    features.default_features.append('h1')


@hooks.register('insert_global_admin_css', order=100)
def global_admin_css():
    return format_html(
      '<link rel="stylesheet" href="{}">',
      static("css/admincustom.css")
    )


@hooks.register('insert_global_admin_css', order=100)
def pykafe_css():
    return format_html(
      '<link rel="stylesheet" href="{}">',
      static("css/pykafe.css")
    )
