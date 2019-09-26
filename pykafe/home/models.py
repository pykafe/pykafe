from django.db import models


from wagtail.core.models import Page
from wagtail.core.fields import RichTextField, StreamField
from modelcluster.fields import ParentalKey
from wagtail.admin.edit_handlers import FieldPanel, StreamFieldPanel
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.snippets.models import register_snippet
from wagtail.snippets.edit_handlers import SnippetChooserPanel

from .blocks import PykafeRichBlock, PageLinksBlock, PykafeMap, LearnRichBlock, CategoryRichBlock, CodeRichBlock


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
        ImageChooserPanel('image'),
        StreamFieldPanel('body'),
    ]
    subpage_types = ["home.BasePage", "contact.ContactPage", "home.LearnContentPage"]


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
        StreamFieldPanel('body'),
        FieldPanel('image_title', classname="full"),
        ImageChooserPanel('image'),
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
                ('categories', CategoryRichBlock(dafault='', null=True, blank=True)),
                ('content', LearnRichBlock(null=True, blank=True)),
                ('code', CodeRichBlock(null=True, blank=True)),
            ]
        )

    content_panels = Page.content_panels + [
        ImageChooserPanel('image'),
        StreamFieldPanel('body'),
    ]

    template = 'home/home_page.html'


# registu ka import funsaun decorator no kria category
@register_snippet
class LearnCategory(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(unique=True, max_length=80)

    panels = [
        FieldPanel('name'),
        FieldPanel('slug'),
    ]

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"

# Kria model koneksaun entre Class LearnContentPage no LearnCategory
class LearnPageLearnCategory(models.Model):
    page = ParentalKey('home.LearnContentPage', on_delete=models.CASCADE)
    learn_category = models.ForeignKey(
        'home.LearnCategory', on_delete=models.CASCADE)

    panels = [
        SnippetChooserPanel('learn_category'),
    ]

    class Meta:
        unique_together = ('page', 'learn_category')
