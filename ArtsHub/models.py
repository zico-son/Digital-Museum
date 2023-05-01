from django.db import models
# Create your models here.
class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        abstract = True

class Hall(BaseModel):
    name = models.CharField(max_length=255)
    # hall.art_object.all()
    def __str__(self):
        return self.name

class ArtObject(BaseModel):
    name = models.CharField(max_length=255)
    epoch = models.CharField(max_length=255)
    description = models.TextField()
    hall = models.ForeignKey(Hall, on_delete=models.CASCADE, related_name='art_object')
    active = models.BooleanField(default=False)
    highlighted = models.BooleanField(default=False)

    def __str__ (self):
        return self.name
    class Meta:
        ordering = ['-created_at']

class ArtObjectImage(BaseModel):
    art_object = models.ForeignKey(ArtObject, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='images/')
    def __str__(self):
        try:
            return self.art_object.name
        except:
            return ""

class ArtStory(BaseModel):
    title = models.CharField(max_length=255)
    description = models.TextField()
    art_object = models.OneToOneField(ArtObject, on_delete=models.CASCADE, related_name='art_story', primary_key=True)
    def __str__(self):
        try:
            return self.art_object.name
        except:
            return ""

class Chariot(BaseModel):
    object_number = models.CharField(max_length=255)
    origin = models.CharField(max_length=255)
    chassis_number = models.CharField(max_length=255)
    art_object = models.OneToOneField(ArtObject, on_delete=models.CASCADE, related_name='chariot', primary_key=True)
    def __str__(self):
        try:
            return self.art_object.name
        except:
            return ""

class Painting(BaseModel):
    artist_name = models.CharField(max_length=255)
    art_object = models.OneToOneField(ArtObject, on_delete=models.CASCADE, related_name='painting', primary_key=True)
    def __str__(self):
        try:
            return self.art_object.name
        except:
            return ""
    

class Other(BaseModel):
    origin = models.CharField(max_length=255)
    art_object = models.OneToOneField(ArtObject, on_delete=models.CASCADE, related_name='other', primary_key=True)
    def __str__(self):
        try:
            return self.art_object.name
        except:
            return ""

class Holding(BaseModel):
    material = models.CharField(max_length=255)
    art_object = models.ForeignKey(ArtObject, on_delete=models.CASCADE, related_name='holdings')
    def __str__(self):
        try:
            return self.art_object.name
        except:
            return ""

class BorrowedCollection(BaseModel):
    date_of_borrowing = models.DateField()
    date_of_return = models.DateField()
    art_object = models.OneToOneField(ArtObject, on_delete=models.CASCADE, related_name='borrowed_collection', primary_key=True)
    def __str__(self):
        try:
            return self.art_object.name
        except:
            return ""

class PermanentCollection(BaseModel):
    date_of_acquisition = models.DateField()
    art_object = models.OneToOneField(ArtObject, on_delete=models.CASCADE, related_name='permanent_collection', primary_key=True)
    def __str__(self):
        try:
            return self.art_object.name
        except:
            return ""