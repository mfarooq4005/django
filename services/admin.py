from django.contrib import admin
from .models import titles
class for_title(admin.ModelAdmin):
    list_display = ('main_title','main_description','image_url')
admin.site.register(titles,for_title)
# Register your models here.
