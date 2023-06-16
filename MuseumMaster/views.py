from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet, ReadOnlyModelViewSet
from .customviewsets import CustomModelViewSet
from .serializers import *
from .models import *

# Create your views here.
class InfoViewSet(ReadOnlyModelViewSet):
    queryset = MuseumInfo.objects.all()
    serializer_class = InfoSerializer

class HotelViewSet(ReadOnlyModelViewSet):
    queryset = Hotels.objects.all()
    serializer_class = HotelSerializer