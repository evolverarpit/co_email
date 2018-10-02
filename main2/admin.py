from django.contrib import admin
from .models import *
class CompanyItemNewAdmin(admin.ModelAdmin):
    list_display = ('name', 'url', 'employees')
    search_fields = ('name', 'url')
    list_per_page = 50

admin.site.register(CompanyItemNew, CompanyItemNewAdmin)

class HunterItemNewAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'pattern')
    search_fields = ('name', 'email')
    list_per_page = 50

admin.site.register(HunterItemNew, HunterItemNewAdmin)
#admin.site.register(CompanyItemNew)
#admin.site.register(HunterItemNew)
#admin.site.register(SourceItemNew)

