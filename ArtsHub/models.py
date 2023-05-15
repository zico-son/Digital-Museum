from django.db import models
from MuseumMaster.models import Media
from ArtsHub.utils import *
from django.contrib import messages
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
    class Meta:
        ordering = ['name'] 

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
    image = models.FileField(upload_to='images/')
    convert_image = models.BooleanField(default=False)
    size_before_convert = models.FloatField(default=0, verbose_name = 'size before convert in MB')
    size_after_convert = models.FloatField(default=0, verbose_name= 'size after convert in MB')
    compression_ratio = models.FloatField(default=0, verbose_name='compression ratio %')
    quality = models.IntegerField(default=50, verbose_name='quality % (default = 50 %)', blank=True)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        if self.convert_image:
            self.size_before_convert = rounding_image_size(get_file_size(self.image.path))          
            image_name = self.image.name
            convert_image(self.image.path, get_image_extension(image_name), get_image_name(image_name), self.quality)
            self.image = get_image_save_path(image_name)
            super().save(*args, **kwargs)
            self.size_after_convert = rounding_image_size(get_file_size(self.image.path))
            rounding_image_size(self.size_after_convert)
            self.compression_ratio = rounding_image_size(get_compression_ratio(self.size_before_convert, self.size_after_convert))
            super().save(*args, **kwargs)

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