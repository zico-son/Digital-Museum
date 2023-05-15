from django.contrib import admin
from django.http.request import HttpRequest
from ArtsHub.models import Hall, ArtObject, ArtStory, Chariot, Painting, Other, Holding, BorrowedCollection, PermanentCollection , ArtObjectImage
from django.contrib import messages
from django.shortcuts import redirect

@admin.register(Hall)
class HallAdmin(admin.ModelAdmin):
    list_per_page = 10

@admin.register(ArtStory)
class ArtStoryAdmin(admin.ModelAdmin):
    def has_delete_permission(self, request, obj=None):
        return False
    def has_add_permission(self, request, obj=None):
        return False
    def has_change_permission(self, request, obj=None):
        return False
    list_per_page = 10
    list_display = ['art_object', 'title']
    search_fields = ['art_object__name', 'title']

@admin.register(Chariot)
class ChariotAdmin(admin.ModelAdmin):
    def has_delete_permission(self, request, obj=None):
        return False
    def has_add_permission(self, request, obj=None):
        return False
    def has_change_permission(self, request, obj=None):
        return False
    list_per_page = 10
    list_display = ['art_object', 'object_number', 'origin', 'chassis_number']
    search_fields = ['art_object__name', 'object_number', 'origin', 'chassis_number']

@admin.register(Painting)
class PaintingAdmin(admin.ModelAdmin):
    def has_delete_permission(self, request, obj=None):
        return False
    def has_add_permission(self, request, obj=None):
        return False
    def has_change_permission(self, request, obj=None):
        return False
    list_per_page = 10
    list_display = ['art_object', 'artist_name']
    search_fields = ['art_object__name', 'artist_name']

@admin.register(Other)
class OtherAdmin(admin.ModelAdmin):
    def has_delete_permission(self, request, obj=None):
        return False
    def has_add_permission(self, request, obj=None):
        return False
    def has_change_permission(self, request, obj=None):
        return False
    list_per_page = 10
    list_display = ['art_object', 'origin']
    search_fields = ['art_object__name', 'origin']

@admin.register(Holding)
class HoldingAdmin(admin.ModelAdmin):
    def has_delete_permission(self, request, obj=None):
        return False
    def has_add_permission(self, request, obj=None):
        return False
    def has_change_permission(self, request, obj=None):
        return False
    list_per_page = 10
    list_display = ['art_object', 'material']
    search_fields = ['art_object__name', 'material']


@admin.register(BorrowedCollection)
class BorrowedCollectionAdmin(admin.ModelAdmin):
    def has_delete_permission(self, request, obj=None):
        return False
    def has_add_permission(self, request, obj=None):
        return False
    def has_change_permission(self, request, obj=None):
        return False
    list_per_page = 10
    list_display = ['art_object', 'date_of_borrowing', 'date_of_return']    
    search_fields = ['art_object__name', 'date_of_borrowing', 'date_of_return']

@admin.register(PermanentCollection)
class PermanentCollectionAdmin(admin.ModelAdmin):
    def has_delete_permission(self, request, obj=None):
        return False
    def has_add_permission(self, request, obj=None):
        return False
    def has_change_permission(self, request, obj=None):
        return False
    list_per_page = 10
    list_display = ['art_object', 'date_of_acquisition']
    search_fields = ['art_object__name', 'date_of_acquisition']

@admin.register(ArtObjectImage)
class ArtObjectImageAdmin(admin.ModelAdmin):
    def has_delete_permission(self, request, obj=None):
        return False
    def has_add_permission(self, request, obj=None):
        return False
    def has_change_permission(self, request, obj=None):
        return False
    list_per_page = 10
    list_display = ['art_object', 'image']
    search_fields = ['art_object__name', 'image']
    readonly_fields = ['size_before_convert','size_after_convert', 'compression_ratio', 'quality']


class ArtStoryInline(admin.StackedInline):
    model = ArtStory
    extra = 0
class ChariotInline(admin.StackedInline):
    model = Chariot
    extra = 0
class PaintingInline(admin.StackedInline):
    model = Painting
    extra = 0
class OtherInline(admin.StackedInline):
    model = Other
    extra = 0
class HoldingInline(admin.StackedInline):
    model = Holding
    extra = 0
class BorrowedCollectionInline(admin.StackedInline):
    model = BorrowedCollection
    extra = 0
class PermanentCollectionInline(admin.StackedInline):
    model = PermanentCollection
    extra = 0
class ArtObjectImageInline(admin.StackedInline):
    model = ArtObjectImage
    extra = 0
    fields = ['image', 'convert_image', 'quality']

@admin.register(ArtObject)
class ArtObjectAdmin(admin.ModelAdmin):
    list_per_page = 10
    list_display = ['name']
    search_fields = ['name' , 'art_story__title']
    list_filter = ['active', 'highlighted', 'hall']
    list_display = ['name', 'active', 'highlighted', 'created_at', 'updated_at']
    list_editable = ['active', 'highlighted']
    inlines = [ArtObjectImageInline, ArtStoryInline,  BorrowedCollectionInline, PermanentCollectionInline,ChariotInline, PaintingInline, OtherInline, HoldingInline ]
    fields = ['name', 'hall', 'description' , 'active', 'highlighted', 'media','created_at', 'updated_at']
    readonly_fields = ['created_at', 'updated_at', 'media']
    queryset = ArtObject.objects \
        .select_related('hall') \
        .prefetch_related('images') \
        .prefetch_related('holdings') \
        .select_related('art_story') \
        .select_related('chariot') \
        .select_related('painting') \
        .select_related('other') \
        .select_related('borrowed_collection') \
        .select_related('permanent_collection') \
        .all()
    def message_user(self):
        pass
    def save_model(self, request, obj, form, change):
        return super().save_model(request, obj, form, change)

    def response_change(self, request, obj):
        try:
            last = obj.images.last().id
        except:
            messages.success(request, f'Art Object updated successfully')
            return redirect(f'/admin/ArtsHub/artobject/')
        if obj.images.last().convert_image:
            messages.success(request, f'Image converted successfully')
            return redirect(f'/admin/ArtsHub/artobjectimage/{last}/change/')
        messages.success(request, f'Art Object updated successfully')
        return redirect(f'/admin/ArtsHub/artobject/')