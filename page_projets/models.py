from django.db import models
from modelcluster.fields import ParentalKey
from wagtail.admin.panels import FieldPanel,MultiFieldPanel,InlinePanel
from django.core.paginator import EmptyPage,PageNotAnInteger,Paginator
from wagtail.models import Page,Orderable
from wagtailseo.models import SeoMixin, SeoType, TwitterCard

class ProjectsPage(SeoMixin,Page):
    max_count = 1 
    subpage_types = ['page_projets.Single_projectPage']

    description = models.CharField(max_length=255, blank=True,)

    content_panels = Page.content_panels + [FieldPanel("description", classname="full")]

    seo_content_type = SeoType.ARTICLE
    seo_twitter_card = TwitterCard.LARGE
    promote_panels = SeoMixin.seo_panels
    
    def get_context(self, request, *args, **kwargs):
        context = super().get_context(request, *args, **kwargs)
        all_post = Single_projectPage.objects.live().order_by('title')
        page = request.GET.get('page')
 
        paginator = Paginator(all_post, 3)
        try:
            post = paginator.page(page)
        except PageNotAnInteger:
            post = paginator.page(1)
        except EmptyPage:
            post = paginator.page(paginator.num_pages)
            
        context['post'] = post
        return context
    
class ElementPageDocument(Orderable):
    page = ParentalKey("page_projets.Single_projectPage", related_name="documents")
    document = models.FileField(upload_to='documents', blank= True)
    
    panels = [ 
        FieldPanel("document"),
    ]


class Single_projectPage(SeoMixin,Page):
    subpage_types = []

    Description = models.CharField(max_length=255, blank=True,)
    Detail = models.TextField()
    Localisation = models.CharField(max_length=255, blank=True,)
    Cible = models.CharField(max_length=255, blank=True,)
    Cout_projet = models.CharField(max_length=255, blank=True,)
    Progression = models.CharField(max_length=255, blank=True,)
    Debut_projet = models.DateField()
    Fin_projet = models.DateField()
    content_panels = Page.content_panels + [
        MultiFieldPanel(
            [
                FieldPanel("Description"),
                FieldPanel("Detail"),
                FieldPanel("Localisation"),
                FieldPanel("Cible"),
                FieldPanel("Cout_projet"),
                FieldPanel("Progression"),
                FieldPanel("Debut_projet"),
                FieldPanel("Fin_projet"),
            ], heading = "Description du projet"
        ),
        MultiFieldPanel(
            [ InlinePanel("documents", max_num = 1, min_num = 1) ]
        ), 
    ]
    
    
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = "Project"
        verbose_name_plural = "Projects"

    seo_content_type = SeoType.ARTICLE
    seo_twitter_card = TwitterCard.LARGE
    promote_panels = SeoMixin.seo_panels