from django.db import models
from modelcluster.fields import ParentalKey
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from wagtail.models import Page
from wagtail.fields import RichTextField
from wagtail.admin.panels import FieldPanel,InlinePanel
from wagtail.snippets.models import register_snippet
from wagtail.fields import StreamField
from wagtail import blocks
from wagtail.images.blocks import ImageChooserBlock

from wagtailseo.models import SeoMixin, SeoType, TwitterCard
from wagtail.search import index


class PostPage(SeoMixin,Page):
    max_count = 1
    subpage_types = ['blog.Single_postPage']
    description = models.CharField(max_length=255, blank=True,)

    content_panels = Page.content_panels + [FieldPanel("description", classname="full")]
    
    def get_context(self, request, *args, **kwargs):
        context = super().get_context(request, *args, **kwargs)
        all_post = Single_postPage.objects.live().order_by('-date')
        page = request.GET.get('page')
 
        paginator = Paginator(all_post, 10)
        try:
            post = paginator.page(page)
        except PageNotAnInteger:
            post = paginator.page(1)
        except EmptyPage:
            post = paginator.page(paginator.num_pages)
            
        context['post'] = post
        return context
    
    seo_content_type = SeoType.ARTICLE
    seo_twitter_card = TwitterCard.LARGE
    promote_panels = SeoMixin.seo_panels
    
    @property
    def blogs(self):
        blogs = Single_postPage.objects.live().order_by('-date')
        blogs = blogs.order_by('-date')

        return blogs
    
    
    @property
    def actu(self):
        actu = Single_postPage.objects.live().order_by('-date')
        actu = actu.order_by('-date')

        return actu
    
    
    @property
    def actus(self):
        actus = Single_postPage.objects.live().order_by('-date')
        actus = actus.order_by('-date')

        return actus
    
   
class Single_postPage(SeoMixin,Page):
    
    subpage_types = []
    
    date = models.DateTimeField(blank=True, null=True)
    body = StreamField([
        ('paragraph', blocks.RichTextBlock()),
        ('image', ImageChooserBlock()),
    ], use_json_field=True)
    image = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",)
    
    search_fields = Page.search_fields + [
        index.SearchField('title'),
    ]

    content_panels = Page.content_panels + [
        FieldPanel("image"),
        FieldPanel("body"),
        FieldPanel('date'),
        InlinePanel("categories", label="Categories"),
        ]
    
    seo_content_type = SeoType.ARTICLE
    seo_twitter_card = TwitterCard.LARGE
    promote_panels = SeoMixin.seo_panels
    
    def __str__(self):
        return self.title
    
        
    def blogs(self):
        
        blogs = Single_postPage.objects.live()
        blogs = blogs.order_by('-date')[:3]

        return blogs
  
    def get_context(self, request):
        context = super(Single_postPage, self).get_context(request)
        context['blogs'] = self.blogs()
        
        return context 
    
    class Meta:
        verbose_name = "Actualité"
        verbose_name_plural = "Actualités"

class PostPageBlogCategory(models.Model):
    page = ParentalKey(
        "blog.Single_postPage", on_delete=models.CASCADE, related_name="categories"
    )
    blog_category = models.ForeignKey(
        "blog.BlogCategory", on_delete=models.CASCADE, related_name="post_pages"
    )

    panels = [
        FieldPanel("blog_category"),
    ]

    class Meta:
        unique_together = ("page", "blog_category")


@register_snippet
class BlogCategory(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(unique=True, max_length=80)
    panels = [
        FieldPanel("name"),
        FieldPanel("slug"),
    ]

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Categorie"
        verbose_name_plural = "Categories"
