from rest_framework import generics
from .models import Aviso
from .serializers import AvisoSerializer
from rest_framework.parsers import FileUploadParser
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from django.db.models.functions import Lower


class AvisoList(generics.ListCreateAPIView):
    serializer_class = AvisoSerializer
    queryset = Aviso.objects.all()
    queryset = Aviso.objects.order_by(Lower('published_date').desc())


class FileUploadView(APIView):
    parser_class = (FileUploadParser,)

    def post(self, request, *args, **kwargs):

        file_serializer = AvisoSerializer(data=request.data)

        if file_serializer.is_valid():
            file_serializer.save()
            return Response(file_serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(file_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
