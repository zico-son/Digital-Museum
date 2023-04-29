from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .customviewsets import CustomModelViewSet
from .serializers import *
from .models import *

# Create your views here.
class InfoViewSet(CustomModelViewSet):
    queryset = MuseumInfo.objects.all()
    serializer_class = InfoSerializer