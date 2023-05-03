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
        
admin.site.register(models.Event)
admin.site.register(models.Media)
admin.site.register(models.MuseumInfo,MuseumInfoAdmin)
admin.site.register(models.OpenningHour)
