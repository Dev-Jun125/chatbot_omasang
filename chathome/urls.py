from django.urls import path, include

from chathome.views import chathome

app_name = "chathome"

urlpatterns = [
    path('', chathome, name='chathome'),
]