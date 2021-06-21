from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views import View
from . import chatbot
from . import dbconnect
from . import comparison
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from chatting.models import Userinput
from chatting.serializers import userinputSerializer
from django.views.decorators.csrf import csrf_exempt


# Create your views here.
@csrf_exempt
def hello(request):
    response = comparison.hello_tip()
    message = {'message' : response[0]}
    return JsonResponse(message)


@csrf_exempt
def basic_Conversation(request, word):
    user_input = ''
    chatbot_respond = ''
    user_input = word
    comparison.userinput(user_input)
    response = comparison.response_select(word)
    while(True):
        message = {
            'message' : response[0][0],
            'message2' : response[1][0],
            'message3' : response[2][0],
            'message4' : response[3][0],
            'message5' : response[4][0],
        }       
        
        return JsonResponse(message)

@api_view(['post'])
def chatAPI(request):
    serializer = userinputSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status = status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)