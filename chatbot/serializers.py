from rest_framework import serializers
from chatbot.models import info, test


class chatbotSerializer(serializers.ModelSerializer):
    class Meta:
        model = info
        fields  = ['created', 'idx', 'message']


class testSerializer(serializers.ModelSerializer):
    class Meta:
        model = test
        fields  = ['idx', 'message']