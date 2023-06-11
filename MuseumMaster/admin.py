from django.contrib import admin
from .models import *
from . import models
from . import*
# Register your models here.
class MuseumInfoAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        if MuseumInfo.objects.count() == 1:
            return False
        return True
        

admin.site.register(models.Media)
admin.site.register(models.MuseumInfo,MuseumInfoAdmin)
admin.site.register(models.OpenningHour)
admin.site.register(models.DownloadableItems)

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_per_page = 10
    list_display = ['name', 'date','start_time', 'end_time', 'active']
    list_filter = ['active','date']
    list_editable = ['active']
    search_fields = ['name']

