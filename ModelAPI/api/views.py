from django.shortcuts import render
from django.http import JsonResponse

# Imports for Image 

from rest_framework import status
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import UploadedImage
from .serializers import UploadedImageSerializer
from rest_framework import viewsets
from rest_framework.parsers import FileUploadParser



def index(request):
    return render(request,'index.html')


def home(request, *args, **kwargs):
    return JsonResponse({"message":"End Point is Working!"})


class UploadedImageViewSet(viewsets.ModelViewSet):
    queryset = UploadedImage.objects.all()
    serializer_class = UploadedImageSerializer
    parser_classes = [FileUploadParser]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)