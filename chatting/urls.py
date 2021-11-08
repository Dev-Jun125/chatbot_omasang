from django.urls import path
from . import views
 
urlpatterns = [
    path('이준현개병신새끼',views.hello),
    path('<word>/', views.basic_Conversation),
    path('test/',views.chatAPI),
]
