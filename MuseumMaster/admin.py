from django.contrib import admin
from . import models
from . import*
# Register your models here.
admin.site.register(models.Event)
admin.site.register(models.Media)
admin.site.register(models.MuseumInfo)
admin.site.register(models.OpenningHour)
