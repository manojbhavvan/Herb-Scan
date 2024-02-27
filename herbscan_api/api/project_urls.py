from django.urls import path, include
from . import urls

urlpatterns = [
    path('api/', include(urls)),
]