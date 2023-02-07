from django.db import models
from wagtail.models import Page
from wagtail.fields import StreamField
from wagtail import blocks
from wagtail.admin.panels import FieldPanel
from wagtailseo.models import SeoMixin, SeoType, TwitterCard
from wagtail.admin.panels import FieldPanel

class AdministrationPage(SeoMixin, Page):
    max_count = 1 
    subpage_types = ['page_ministere.Single_biographyPage']
    description = models.CharField(max_length=255, blank=True,)
    petit_detail = models.CharField(max_length=255)
    content_panels = Page.content_panels + [
        FieldPanel("description", classname="full"),
        FieldPanel('petit_detail'),
    ]
    
    seo_content_type = SeoType.ARTICLE
    seo_twitter_card = TwitterCard.LARGE
    promote_panels = SeoMixin.seo_panels
    
    def get_context(self, request, *args, **kwargs):
        context = super().get_context(request, *args, **kwargs)
        context['post'] = Single_biographyPage.objects.live()
        return context
    
    @property
    def min(self):
        min = AdministrationPage.objects.live()
        min = min.order_by('title')

        return min
    
    @property
    def minis(self):
        minis = Single_biographyPage.objects.live()
        minis = minis.order_by('title')

        return minis

    @property
    def sec(self):
        sec = Single_biographyPage.objects.live()
        sec = sec.order_by('title')

        return sec

class Single_biographyPage(SeoMixin, Page):
    subpage_types = []
    
    fonction = models.CharField(max_length=255)
    petit_detail = models.CharField(max_length=255)
    image = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",)
    
    body = StreamField([
        ('heading', blocks.CharBlock(form_classname="full title")),
        ('paragraph', blocks.RichTextBlock()),
        ('liste', blocks.ListBlock(blocks.RichTextBlock())),
        
    ], use_json_field=True)

    content_panels = Page.content_panels + [
        FieldPanel('fonction'),
        FieldPanel("image"),
        FieldPanel('petit_detail'),
        FieldPanel('body'),
    ]

    seo_content_type = SeoType.ARTICLE
    seo_twitter_card = TwitterCard.LARGE
    promote_panels = SeoMixin.seo_panels
    
    def __str__(self):
        return self.title
    
   
    
    class Meta:
        verbose_name = "Ministère"
        verbose_name_plural = "Ministère"
