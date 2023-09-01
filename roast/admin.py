from django.contrib import admin
from .models import news
class newsAdmin(admin.ModelAdmin):
    list_display=('title','desc')
admin.site.register(news,newsAdmin)
# Register your models here.