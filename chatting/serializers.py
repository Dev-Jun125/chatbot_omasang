from rest_framework import serializers
from django.contrib.auth.models import User, Group
from chatting.models import Userinput

class userinputSerializer(serializers.ModelSerializer):
    class Meta:
        model = Userinput
        fields = ['userinput']