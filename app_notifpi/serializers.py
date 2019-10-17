from rest_framework import serializers
from .models import Aviso

class AvisoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Aviso
        fields = ('audio_descrip')