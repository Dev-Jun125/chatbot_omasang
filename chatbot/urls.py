from django.urls import path
from chatbot import views
from django.contrib import admin

urlpatterns = [
    path('chatbot/', views.chatbot_list),
    path('chatbot/<int:pk>/', views.chatbot_detail),
    path('admin/', admin.site.urls),
    path('test/', views.test_list),
]