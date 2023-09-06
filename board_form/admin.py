from django.contrib import admin
from .models import Result

#@admin.register(Result)
class ResultAdmin(admin.ModelAdmin):
    list_display = ('maths', 'eng', 'urdu', 'biy', 'phy', 'chy', 'ist', 'ps', 'total_numbers', 'percentage', 'division','image_selection')
admin.site.register(Result,ResultAdmin)

# Optionally, if you want to use a custom admin site (BoardResult), you can do so like this:
# class BoardResultAdminSite(admin.AdminSite):
#     site_header = 'Custom Admin Site Header'
#     site_title = 'Custom Admin Site Title'
#
# board_admin_site = BoardResultAdminSite(name='boardadmin')
# board_admin_site.register(Result, ResultAdmin)
