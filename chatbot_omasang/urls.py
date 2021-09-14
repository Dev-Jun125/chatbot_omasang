from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from rest_framework import routers
from django.contrib import admin

urlpatterns = [
    path('', include('chatbot.urls')),
    path('chatting/', include('chatting.urls')),
    path('chathome/', include('chathome.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)