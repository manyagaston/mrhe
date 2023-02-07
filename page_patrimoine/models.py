from django.db import models
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from wagtail.admin.panels import FieldPanel,MultiFieldPanel,InlinePanel
from wagtail.models import Page
from wagtail.fields import RichTextField
from wagtail.fields import StreamField
from wagtail import blocks
from wagtailseo.models import SeoMixin, SeoType, TwitterCard


class National_heritagePage(SeoMixin, Page):
    max_count = 1 
    subpage_types = ['page_patrimoine.DetailPage']
    
    description = models.CharField(max_length=255, blank=True,)

    content_panels = Page.content_panels + [FieldPanel("description", classname="full")]
   
    seo_content_type = SeoType.ARTICLE
    seo_twitter_card = TwitterCard.LARGE
    promote_panels = SeoMixin.seo_panels
    
    def get_context(self, request, *args, **kwargs):
        context = super().get_context(request, *args, **kwargs)
        all_post = DetailPage.objects.live()
        page = request.GET.get('page')
        
        paginator = Paginator(all_post, 2)
        try:
            post = paginator.page(page)
        except PageNotAnInteger:
            post = paginator.page(1)
        except EmptyPage:
            post = paginator.page(paginator.num_pages)
            
        context['post'] = post
        return context
    
    
   
class DetailPage(SeoMixin, Page):
    
    subpage_types = []

    description = models.CharField(max_length=255, blank=True,)
    body = RichTextField(features=['anchor-identifier', 'h2', 'h3', 'bold', 'italic', 'link'])
    header_image = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",)
    
    Table = StreamField([
        ('Acces_rapide', blocks.StructBlock([
            ("Titre_de_l_ancre", blocks.CharBlock(required=True, max_length=40, help_text="Saisir le texte du Titre. Ex : Mettre à jour les photos ")),
            ("Lien_d_ancre", blocks.TextBlock(help_text="Saisir l'ancre de lien. Ex : #mettre-a-jour-les-photos")),
        
        ], icon='edit')),
    ], use_json_field=True)


    content_panels = Page.content_panels + [
        FieldPanel("description"),
        FieldPanel("body"),
        FieldPanel("header_image"),
      MultiFieldPanel(
            [ 
                FieldPanel("Table"),
            ]
        ), 
        ]
        
    seo_content_type = SeoType.ARTICLE
    seo_twitter_card = TwitterCard.LARGE
    promote_panels = SeoMixin.seo_panels
    
    def __str__(self):
        return self.title
    
   
    class Meta:
        verbose_name = "Patrimoine nationale"
        verbose_name_plural = "Patrimoine nationale"
