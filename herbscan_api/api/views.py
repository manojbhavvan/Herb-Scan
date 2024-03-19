# from django.shortcuts import render
# from rest_framework import viewsets, status
# from rest_framework.parsers import MultiPartParser
# from rest_framework.response import Response
# from .models import ImageUpload
# from .serializers import ImageUploadSerializer

# # Create your views here.
# class ImageUploadViewSet(viewsets.ModelViewSet):
#     queryset = ImageUpload.objects.all()
#     serializer_class = ImageUploadSerializer
#     parser_class = [MultiPartParser]

#     def create(self, request, *args, **kwargs):
#         serializer = self.get_serializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         self.perform_create(serializer)
#         headers = self.get_success_headers(serializer.data)
#         return Response(serializer.data, status=status.HTTP_201_CREATED, headers = headers)

from rest_framework import viewsets, status
from rest_framework.parsers import MultiPartParser
from rest_framework.response import Response
import os
from .image_utils import predict_plant
from django.conf import settings

class ImageUploadViewSet(viewsets.ViewSet):
    parser_class = [MultiPartParser]

    def create(self, request, *args, **kwargs):
        # Get the uploaded image file
        uploaded_file = request.FILES["image"]

        # Generate a unique filename and save to media folder
        filename = f"plants/{uploaded_file.name}"
        filepath = os.path.join(settings.MEDIA_ROOT, filename)
        with open(filepath, "wb") as f:
            for chunk in uploaded_file.chunks():
                f.write(chunk)

        # Perform prediction using the saved image path
        predicted_label, confidence = predict_plant(filepath)

        # Cleanup (optional, you might keep the uploaded image)
        os.remove(filepath)

        # Return prediction results
        return Response(
            {"predicted_label": predicted_label, "confidence": float(confidence)},
            status=status.HTTP_200_OK,
        )
