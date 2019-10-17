from django.shortcuts import render
from rest_framework import generics
from .models import Aviso
from .serializers import AvisoSerializer

class AvisoList(generics.ListCreateAPIView):

    serializer_class = AvisoSerializer
