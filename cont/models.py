from django.db import models

from django.core.mail import send_mail
from django.conf import settings


from wagtail.contrib.forms.models import AbstractEmailForm, AbstractFormField
from wagtailcaptcha.models import WagtailCaptchaEmailForm
from modelcluster.fields import ParentalKey
from wagtail.fields import RichTextField
from wagtail.admin.panels import FieldPanel,InlinePanel,MultiFieldPanel,FieldRowPanel
from functools import cached_property

class FormField(AbstractFormField):
    
    page = ParentalKey("ContactPage",on_delete=models.CASCADE, related_name="form_fields")


class ContactPage(WagtailCaptchaEmailForm):
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

    def email(request):    
        subject = 'Thank you for registering to our site'
        message = ' it  means a world to us '
        email_from = settings.EMAIL_HOST_USER
        recipient_list = ['apictvoficiell@gmail.com',]    

        send_mail( subject, message, email_from, recipient_list )    
        return redirect('redirect to a new page')