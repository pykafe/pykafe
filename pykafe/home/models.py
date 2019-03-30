from django.db import models

from wagtail.core import blocks
from wagtail.core.models import Page
from wagtail.core.fields import RichTextField, StreamField
from wagtail.admin.edit_handlers import FieldPanel, StreamFieldPanel
from wagtail.images.edit_handlers import ImageChooserPanel

from .blocks import PykafeRichBlock

class HomePage(Page):
    image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+')

    body = StreamField([('paragraph', PykafeRichBlock())])

    content_panels = Page.content_panels + [
        ImageChooserPanel('image'),
        StreamFieldPanel('body'),
    ]
    subpage_types = ["home.BasePage"]

class StyleGuidePage(Page):
    content = RichTextField(blank=True)

    content_panels = Page.content_panels + [
        FieldPanel('content', classname="full")
    ]


class BasePage(Page):
    body = StreamField([('paragraph', PykafeRichBlock())])

    content_panels = Page.content_panels + [
        StreamFieldPanel('body')
    ]
