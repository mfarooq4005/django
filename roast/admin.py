from django.contrib import admin
from .models import News
class newsAdmin(admin.ModelAdmin):
    list_display=('news_title','news_desc')
admin.site.register(News,newsAdmin)
# Register your models here.