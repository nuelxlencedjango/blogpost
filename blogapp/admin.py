from django.contrib import admin

from .models import *
# Register your models here.

class PostAdmin(admin.ModelAdmin):
    list_display = ['title','content','date_posted','author']


#class PriceAdmin(admin.ModelAdmin):
#    list_display = ['name','price', 'slug' ,'digital']


admin.site.register(Post ,PostAdmin)

# Register your models here.
