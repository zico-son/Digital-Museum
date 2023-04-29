from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from .models import *

class OpenningHourSerializer(ModelSerializer):
    class Meta:
        model = OpenningHour
        fields = ['day','open_time','close_time']

class MediaSerializer(ModelSerializer):
    class Meta:
        model = Media
        fields = ['media','name']

class EventSerializer(ModelSerializer):
    class Meta:
        model = Event
        fields = ['name','date','start_time','end_time','event_about']

class InfoSerializer(ModelSerializer):
    event = EventSerializer(many =True)
    media = MediaSerializer(many =True)
    openinghours = OpenningHourSerializer(many =True)
    class Meta:
        model = MuseumInfo
        fields = ['name','about','contact_mail','contact_phone','address','event','media','openinghours']

