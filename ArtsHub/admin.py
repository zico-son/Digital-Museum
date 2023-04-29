from django.contrib import admin
from ArtsHub.models import Hall, ArtObject, ArtStory, Chariot, Painting, Other, Holding, BorrowedCollection, PermenatantCollection , ArtObjectImage

class ArtStoryInline(admin.StackedInline):
    model = ArtStory
    extra = 1

@admin.register(Hall)
class HallAdmin(admin.ModelAdmin):
    pass

@admin.register(ArtObject)
class ArtObjectAdmin(admin.ModelAdmin):
    inlines = [ArtStoryInline]

@admin.register(ArtStory)
class ArtStoryAdmin(admin.ModelAdmin):
    pass

@admin.register(Chariot)
class ChariotAdmin(admin.ModelAdmin):
    pass

@admin.register(Painting)
class PaintingAdmin(admin.ModelAdmin):
    pass

@admin.register(Other)
class OtherAdmin(admin.ModelAdmin):
    pass

@admin.register(Holding)
class HoldingAdmin(admin.ModelAdmin):
    pass

@admin.register(BorrowedCollection)
class BorrowedCollectionAdmin(admin.ModelAdmin):
    pass

@admin.register(PermenatantCollection)
class PermenatantCollectionAdmin(admin.ModelAdmin):
    pass

@admin.register(ArtObjectImage)
class ArtObjectImageAdmin(admin.ModelAdmin):
    pass

