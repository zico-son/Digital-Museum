from django.contrib import admin
from .models import *
# Register your models here.
@admin.register(Ticket)
class OtherAdmin(admin.ModelAdmin):
    def has_delete_permission(self, request, obj=None):
        return True
    def has_add_permission(self, request, obj=None):
        return True
    def has_change_permission(self, request, obj=None):
        return True
    list_per_page = 10
    list_display = ['ticket_type', 'price']
    search_fields = ['ticket_type']

@admin.register(Order)
class OtherAdmin(admin.ModelAdmin):
    def has_delete_permission(self, request, obj=None):
        return True
    def has_add_permission(self, request, obj=None):
        return False
    def has_change_permission(self, request, obj=None):
        return False
    list_per_page = 10
    list_display = ['id','name','email','date','created_at']
    search_fields = ['email','date']