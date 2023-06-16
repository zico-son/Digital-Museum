from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from ArtsHub.serializers import ArtObjectSerializer
from ArtsHub.models import ArtObject
from .models import *

class OpenningHourSerializer(ModelSerializer):
    class Meta:
        model = OpenningHour
        fields = ['day','open_time','close_time']

class MediaSerializer(ModelSerializer):
    art_objects = serializers.SerializerMethodField()
    class Meta:
        model = Media
        fields = ['media','name' , 'art_objects']
    
    def get_art_objects(self, obj):
        art_objects = ArtObject.objects.select_related('hall', 'art_story', 'chariot', 'painting', 'other', 'borrowed_collection', 'permanent_collection').prefetch_related('images', 'holdings').filter(highlighted = True)
        return ArtObjectSerializer(art_objects, many = True).data

class EventSerializer(ModelSerializer):
    class Meta:
        model = Event
        fields = ['name','date','start_time','end_time','event_about']

class DownloadableItemsSerializer(ModelSerializer):
    class Meta:
        model = DownloadableItems
        fields = ['name','link']

class InfoSerializer(ModelSerializer):
    event = serializers.SerializerMethodField()
    media = MediaSerializer(many =True)
    openinghours = OpenningHourSerializer(many =True)   
    downloadableItems = DownloadableItemsSerializer(many = True)
    class Meta:
        model = MuseumInfo
        fields = ['name','about','contact_mail','contact_phone','address','event','media','openinghours','downloadableItems']

    def get_event(self, obj):
        event = Event.objects.filter(active = True)
        return EventSerializer(event, many = True).data


class HotelSerializer(ModelSerializer):
    class Meta:
        model = Hotels
        fields = ['id', 'name','address','about','rating','link','image']
