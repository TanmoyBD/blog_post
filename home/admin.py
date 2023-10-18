from django.contrib import admin
from .models import *


admin.site.register(Profile)
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields={'slug':('category_name',)}
    list_display=['category_name','slug']
    
class BlogAdmin(admin.ModelAdmin):
    prepopulated_fields={'slug':('title',)}
    list_display=['title','slug']
    
    
    

admin.site.register(BlogPost,BlogAdmin)
admin.site.register(Category,CategoryAdmin)    

admin.site.register(Rating)
admin.site.register(Comment)
admin.site.register(Favorite)