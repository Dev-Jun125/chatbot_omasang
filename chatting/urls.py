from django.urls import path
from . import views
 
urlpatterns = [
    path('',views.hello),
    path('<word>/', views.basic_Conversation),
    path('test/',views.chatAPI),
]
