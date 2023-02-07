from django.db import models
from modelcluster.fields import ParentalKey
from wagtail.admin.panels import FieldPanel,MultiFieldPanel,InlinePanel
from django.core.paginator import EmptyPage,PageNotAnInteger,Paginator
from wagtail.models import Page,Orderable
from wagtailseo.models import SeoMixin, SeoType, TwitterCard
from wagtail.fields import StreamField
from wagtail import blocks
from wagtail.documents.blocks import DocumentChooserBlock


class Public_PoliciesPage(SeoMixin, Page):
    max_count = 1 
    subpage_types = []

    description = models.CharField(max_length=300, blank=True,)

    document = StreamField([
        ('Article', blocks.StructBlock([
            ("Description", blocks.CharBlock(required=True, max_length=40,  help_text="Ajouter la description ")),
            ("text", blocks.TextBlock(required=True,max_length=255)),

        ('Document', blocks.StreamBlock([
           ('Ajouter', DocumentChooserBlock(required=False,)),
        
        ],min_num=1, max_num=2,)),

        ], icon='cogs')),
    ],min_num=1, max_num=4, use_json_field=True)

   

    content_panels = Page.content_panels + [
        FieldPanel("description", classname="full"),
        MultiFieldPanel(
            [ 
                FieldPanel("document"),
            ]
        ), 
        
        ]
    
    seo_content_type = SeoType.ARTICLE
    seo_twitter_card = TwitterCard.LARGE
    promote_panels = SeoMixin.seo_panels
  
   
    class Meta:
        verbose_name = "Politique Publique"
        verbose_name_plural = "Politique Publique"
