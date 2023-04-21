from django.db import models
from wagtail.models import Page
from wagtail.fields import RichTextField, StreamField
from wagtail.contrib.forms.models import AbstractEmailForm, AbstractFormField
from modelcluster.fields import ParentalKey
#from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.admin.panels import (
    FieldPanel,
    FieldRowPanel,
    InlinePanel,
    MultiFieldPanel,
    StreamFieldPanel
)

from django.forms.fields import EmailField
#from wagtail.admin.utils import send_mail
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from datetime import date
from home.blocks import PykafeMap
from wagtailcaptcha.models import WagtailCaptchaEmailForm

# Create your models here.

class FormField(AbstractFormField):
    page = ParentalKey('ContactPage', on_delete=models.CASCADE, related_name='custom_form_fields')


class ContactPage(WagtailCaptchaEmailForm):
    image_title = models.CharField(max_length=255, blank=True,)
    image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+')
    intro = RichTextField(blank=True)
    thank_you_text = RichTextField(blank=True)
    body = StreamField(
            [
                ('map', PykafeMap())
            ]
        )

    content_panels = AbstractEmailForm.content_panels + [
        InlinePanel('custom_form_fields', label="Form fields"),
        FieldPanel('image_title', classname="full"),
        FieldPanel('image'),
        FieldPanel('intro', classname="full"),
        FieldPanel('body'),
        FieldPanel('thank_you_text', classname="full"),
        MultiFieldPanel([
            FieldRowPanel([
                FieldPanel('from_address', classname="col6"),
                FieldPanel('to_address', classname="col6"),
            ]),
            FieldPanel('subject'),
        ], heading="Email Settings"),
    ]

    def get_form_fields(self):
        return self.custom_form_fields.all()

    def send_mail(self, form):
        addresses = [x.strip() for x in self.to_address.split(',')]
        content_dict = {}
        for field in form:
            value = field.value()
            if isinstance(value, list):
                value = ', '.join(value)
            content_dict.update({ field.label: value })
        submitted_date_str = date.today().strftime('%d %b %Y %H:%M %p')
        content_dict.update({'Submitted': submitted_date_str})
        content_dict.update({'Submitted_Via': self.full_url})
        content_html = render_to_string('contact/contact_us_email.html', content_dict)
        messages = EmailMultiAlternatives(self.subject, content_html, self.from_address, [addresses])
        messages.mixed_subtype = 'related'
        messages.attach_alternative(content_html, "text/html")
        messages.send()
