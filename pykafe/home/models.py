from django.db import models
from wagtail.models import Page
from wagtail.fields import RichTextField, StreamField
from wagtail.admin.panels import FieldPanel
from wagtail.snippets.models import register_snippet

from .blocks import PykafeRichBlock, PageLinksBlock, PykafeMap, LearnRichBlock, PageLearnRichBlock, CodeRichBlock, TableStreamBlock, CategoryTypeRichBlock


class HomePage(Page):
    image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+')

    body = StreamField(
            [
                ('paragraph', PykafeRichBlock()),
                ('links', PageLinksBlock()),
                ('map', PykafeMap())
            ]
        )

    content_panels = Page.content_panels + [
        FieldPanel('image'),
        FieldPanel('body'),
    ]
    subpage_types = ["home.BasePage",
                     "contact.ContactPage",
                     "home.LearnContentPage"]


class StyleGuidePage(Page):
    content = RichTextField(blank=True)

    content_panels = Page.content_panels + [
        FieldPanel('content', classname="full")
    ]


class BasePage(Page):
    image_title = models.CharField(max_length=255, blank=True,)
    image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+')
    description = RichTextField(blank=True, features=['bold', 'italic'])
    body = StreamField([
                ('paragraph', PykafeRichBlock())
        ], blank=True)

    content_panels = Page.content_panels + [
        FieldPanel('show_in_menus', classname="full"),
        FieldPanel('body'),
        FieldPanel('image_title', classname="full"),
        FieldPanel('image'),
        FieldPanel('description')
    ]


# kria Pajina kontent nian
class LearnContentPage(Page):
    image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+')

    body = StreamField(
            [
                ('Pages', PageLearnRichBlock(null=True, blank=True)),
            ]
        )

    content_panels = Page.content_panels + [
        FieldPanel('image'),
        FieldPanel('body'),
    ]


class SubLearnContentPage(Page):
    category = models.CharField(max_length=255, blank=True, null=True)

    body = StreamField(
            [
                ('category_type', CategoryTypeRichBlock(null=True, blank=True)),
                ('content', LearnRichBlock(null=True, blank=True)),
                ('code', CodeRichBlock(null=True, blank=True)),
                ('table', TableStreamBlock(null=True, blank=True)),
            ]
    )

    content_panels = Page.content_panels + [
        FieldPanel('category', classname="full"),
        FieldPanel('body'),
    ]


@register_snippet
class LearnCategory_type(models.Model):
    name = models.CharField(max_length=255, null=True, blank=True)

    panels = [
        FieldPanel('name'),
    ]

    def __str__(self):
        return self.name
