from django.db import models
from MuseumMaster.models import Media
# Create your models here.
class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        abstract = True

class Hall(models.Model):
    name = models.CharField(max_length=255)
    # hall.art_object.all()
    def __str__(self):
        return self.name

class ArtObject(BaseModel):
    name = models.CharField(max_length=255)
    epoch = models.CharField(max_length=255)
    description = models.TextField()
    hall = models.ForeignKey(Hall, on_delete=models.SET_DEFAULT, related_name='art_object', default=8)
    active = models.BooleanField(default=False)
    highlighted = models.BooleanField(default=False)
    media = models.ForeignKey(Media, related_name='art_objects', on_delete=models.PROTECT, default=1)

    def __str__ (self):
        return self.name
    class Meta:
        ordering = ['-created_at']

class ArtObjectImage(models.Model):
    art_object = models.ForeignKey(ArtObject, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='images/')
    def __str__(self):
        try:
            return self.art_object.name
        except:
            return ""

class ArtStory(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    art_object = models.OneToOneField(ArtObject, on_delete=models.CASCADE, related_name='art_story', primary_key=True)
    def __str__(self):
        try:
            return self.art_object.name
        except:
            return ""

class Chariot(models.Model):
    object_number = models.CharField(max_length=255)
    origin = models.CharField(max_length=255)
    chassis_number = models.CharField(max_length=255)
    art_object = models.OneToOneField(ArtObject, on_delete=models.CASCADE, related_name='chariot', primary_key=True)
    def __str__(self):
        try:
            return self.art_object.name
        except:
            return ""

class Painting(models.Model):
    artist_name = models.CharField(max_length=255)
    art_object = models.OneToOneField(ArtObject, on_delete=models.CASCADE, related_name='painting', primary_key=True)
    def __str__(self):
        try:
            return self.art_object.name
        except:
            return ""
    

class Other(models.Model):
    origin = models.CharField(max_length=255)
    art_object = models.OneToOneField(ArtObject, on_delete=models.CASCADE, related_name='other', primary_key=True)
    def __str__(self):
        try:
            return self.art_object.name
        except:
            return ""

class Holding(models.Model):
    material = models.CharField(max_length=255)
    art_object = models.ForeignKey(ArtObject, on_delete=models.CASCADE, related_name='holdings')
    def __str__(self):
        try:
            return self.art_object.name
        except:
            return ""

class BorrowedCollection(models.Model):
    date_of_borrowing = models.DateField()
    date_of_return = models.DateField()
    art_object = models.OneToOneField(ArtObject, on_delete=models.CASCADE, related_name='borrowed_collection', primary_key=True)
    def __str__(self):
        try:
            return self.art_object.name
        except:
            return ""

class PermanentCollection(models.Model):
    date_of_acquisition = models.DateField()
    art_object = models.OneToOneField(ArtObject, on_delete=models.CASCADE, related_name='permanent_collection', primary_key=True)
    def __str__(self):
        try:
            return self.art_object.name
        except:
            return ""