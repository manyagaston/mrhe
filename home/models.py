from wagtail.models import Page,Orderable
from django.db import models
from wagtail.admin.panels import FieldPanel
from wagtailseo.models import SeoMixin, SeoType, TwitterCard
from wagtail.admin.panels import FieldPanel,MultiFieldPanel,InlinePanel,PageChooserPanel
from wagtail.fields import StreamField
from wagtail import blocks
from wagtail.images.blocks import ImageChooserBlock
from blog.models import Single_postPage
from page_ministere.models import Single_biographyPage
from modelcluster.fields import ParentalKey


class HomePage(SeoMixin, Page):
    
    introduction = models.CharField(max_length=255, blank=True, null=True)
    image_fond = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=False,
        on_delete=models.SET_NULL,
        related_name="+"
    ) 

    image = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=False,
        on_delete=models.SET_NULL,
        related_name="+"
    ) 
    administration_du_ministere = StreamField([
        ('administration', blocks.StructBlock([
            ("Description", blocks.CharBlock(required=True, max_length=40,  help_text="Ajouter la description ")),
            ("text", blocks.TextBlock(required=True,max_length=255)),
            ('photo', ImageChooserBlock(required=False)),

        ], icon='user')),
    ],min_num=1, max_num=1, use_json_field=True)

    Secretariat_general = StreamField([
        ('secretariat', blocks.StructBlock([
            ("Description", blocks.CharBlock(required=True, max_length=40,  help_text="Ajouter la description ")),
            ("text", blocks.TextBlock(required=True,max_length=500)),
            ('photo', ImageChooserBlock(required=False)),

        ], icon='edit')),
    ],min_num=1, max_num=1, use_json_field=True)

    agence = StreamField([
        ('cards', blocks.StructBlock([
            ("title", blocks.CharBlock(required=True, max_length=40,  help_text="Ajouter le titre de l'agence ")),
            ("text", blocks.TextBlock(required=True,max_length=500)),
            ("buttton_page", blocks.PageChooserBlock(required=False)),
            ("button_url", blocks.URLBlock(required=False)),
        ])),
    ],min_num=1, max_num=4, use_json_field=True)

    
    content_panels = Page.content_panels + [
        FieldPanel("introduction"),
        FieldPanel("image"),
        FieldPanel("image_fond"),

        MultiFieldPanel(
            [ 
                FieldPanel("administration_du_ministere"),
            ]
        ), 
        MultiFieldPanel(
            [ 
                FieldPanel("Secretariat_general"),
            ]
        ), 
        MultiFieldPanel(
            [ 
                FieldPanel("agence"),
            ], heading = "Agence affiliées"
        ), 
        
    ]

    seo_content_type = SeoType.ARTICLE
    seo_twitter_card = TwitterCard.LARGE
    promote_panels = SeoMixin.seo_panels


    
    def blogs(self):
        
        blogs = Single_postPage.objects.live()
        blogs = blogs.order_by('-date')[:3]

        return blogs
    
    def actu(self):
            
        actu = Single_postPage.objects.live()
        actu = actu.order_by('-date')[3:4]

        return actu
    
    def actus(self):
            
        actus = Single_postPage.objects.live()
        actus = actus.order_by('-date')[4:9]

        return actus
    
    def minis(self):
        minis = Single_biographyPage.objects.live()
        minis = minis.order_by('first_published_at')[:3]

        return minis
    

    
    def get_context(self, request):
        context = super(HomePage, self).get_context(request)
        context['blogs'] = self.blogs()
        context['actu'] = self.actu()
        context['actus'] = self.actus()
        context['minis'] = self.minis()
        
        return context 