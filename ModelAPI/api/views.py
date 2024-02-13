from django.shortcuts import render
from django.http import JsonResponse
# Imports for Image 

from rest_framework import status
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Image
from .serializers import ImageSerializer


def home(request, *args, **kwargs):
    return JsonResponse({"message":"End Point is Working!"})
