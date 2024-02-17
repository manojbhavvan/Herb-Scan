from django.urls import path, include
from django.http import JsonResponse
from . import views
from .views import UploadedImage
from rest_framework.routers import DefaultRouter
from .views import UploadedImageViewSet

router = DefaultRouter()
router.register(r'images', UploadedImageViewSet, basename='image')

urlpatterns = [
    path('', include(router.urls)),
]

# urlpatterns = [
#     path('', views.home),
#     path('image/<str:base64_data>/',views.get_image),
#     path('index/', views.index),
# ]