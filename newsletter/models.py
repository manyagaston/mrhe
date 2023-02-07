from django.db import models

from birdsong.blocks import DefaultBlocks
from birdsong.models import Campaign

from wagtail.admin.panels import StreamFieldPanel, FieldPanel
from wagtail.fields import StreamField


class Newsletter(Campaign):
    headline = models.CharField(
        max_length=255,
        help_text="The headline to use for the newsletter."
    )

    header_background = models.ForeignKey(
        "wagtailimages.Image",
        blank=False,
        null=True,
        related_name="+",
        help_text="The image to use for the header backgound.",
        on_delete=models.SET_NULL,
    )

    body = StreamField(DefaultBlocks())

    panels = Campaign.panels + [
        FieldPanel("headline"),
        FieldPanel("header_background"),
        StreamFieldPanel("body"),
    ]