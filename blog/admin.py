from wagtail.contrib.modeladmin.options import (
ModelAdmin,
modeladmin_register,
)
from .models import Single_postPage

class Single_postPageAdmin(ModelAdmin):
    
    model = Single_postPage
    menu_label = "Articles"
    subpage_types = ['blog.Single_postPage']
    menu_icon = "plus"
    menu_order = 290
    add_to_setings_menu = False
    exclude_from_explorer = False
    list_display = ("title",)
    search_fields = ("title",)
    
modeladmin_register(Single_postPageAdmin)
