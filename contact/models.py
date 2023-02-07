from django.db import models

from wagtail.contrib.forms.models import AbstractEmailForm, AbstractFormField
from wagtailcaptcha.models import WagtailCaptchaEmailForm
from wagtailseo.models import SeoMixin, SeoType, TwitterCard
from modelcluster.fields import ParentalKey
from wagtail.fields import RichTextField
from wagtail.admin.panels import FieldPanel,InlinePanel,MultiFieldPanel,FieldRowPanel
from functools import cached_property

class FormField(AbstractFormField):
    
    page = ParentalKey("ContactPage",on_delete=models.CASCADE, related_name="form_fields")


class ContactPage(SeoMixin, AbstractEmailForm):
    max_count = 1
    subpage_types = []
    intro = RichTextField(blank=True)
    thank_you_text = RichTextField(blank=True)

    content_panels = AbstractEmailForm.content_panels + [
        
        FieldPanel("intro"),
        InlinePanel("form_fields", label="Form fields"),
        FieldPanel("thank_you_text", classname="full"),
        MultiFieldPanel(
            [
                FieldRowPanel(
                    [
                        FieldPanel("from_address", classname="col6"),
                        FieldPanel("to_address", classname="col6"),
                    ]
                ),
                FieldPanel("subject"),
            ],
            "Email Notification Config",
           
        ),
    ]

    
    promote_panels = SeoMixin.seo_panels