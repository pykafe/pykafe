from django.db import models
from wagtail.core.models import Page
from wagtail.core.fields import RichTextField, StreamField
from wagtail.contrib.forms.models import AbstractEmailForm, AbstractFormField
from modelcluster.fields import ParentalKey
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.admin.edit_handlers import (
    FieldPanel,
    FieldRowPanel,
    InlinePanel,
    MultiFieldPanel
)

from django.forms.fields import EmailField
from wagtail.admin.utils import send_mail
from datetime import date

# Create your models here.

class FormField(AbstractFormField):
    page = ParentalKey('ContactPage', on_delete=models.CASCADE, related_name='custom_form_fields')


class ContactPage(AbstractEmailForm):
    image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+')
    intro = RichTextField(blank=True)
    thank_you_text = RichTextField(blank=True)

    content_panels = AbstractEmailForm.content_panels + [
        InlinePanel('custom_form_fields', label="Form fields"),
        ImageChooserPanel('image'),
        FieldPanel('intro', classname="full"),
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
        content = []
        for field in form:
            value = field.value()
            if isinstance(value, list):
                value = ', '.join(value)
            content.append('{}: {}'.format(field.label, value))
        submitted_date_str = date.today().strftime('%x')
        content.append('{}: {}'.format('Submitted', submitted_date_str))
        content.append('{}: {}'.format('Submitted Via', self.full_url))
        content = '\n'.join(content)
        subject = self.subject + " - " + submitted_date_str
        send_mail(subject, content, addresses, self.from_address)
