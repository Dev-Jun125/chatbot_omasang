from django.urls import path, include
from rest_framework import routers
from django.contrib import admin

urlpatterns = [
    path('', include('chatbot.urls')),
    path('chatting/', include('chatting.urls')),
    
]