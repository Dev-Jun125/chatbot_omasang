from django.shortcuts import render, get_object_or_404
from rest_framework.response import Response
from rest_framework.decorators import api_view
from chatbot.models import info, test
from .serializers import chatbotSerializer, testSerializer
from rest_framework import viewsets
from rest_framework import permissions
from django.views import View
from django.views import generic
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser

# Create your views here.
@csrf_exempt
def chatbot_list(request):
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == 'GET':
        infos = info.objects.all()
        serializer = chatbotSerializer(infos, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = chatbotSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)


@csrf_exempt
def chatbot_detail(request, pk):
    """
    Retrieve, update or delete a code snippet.
    """
    try:
        infos = get_object_or_404(info, pk=pk)
    except infos.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = chatbotSerializer(infos)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = chatbotSerializer(infos, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        info.delete()
        return HttpResponse(status=204)

@csrf_exempt
def test_list(request):
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == 'GET':
        tests = test.objects.all()
        serializer = testSerializer(tests, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = testSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

@csrf_exempt
def test_detail(request, pk):
    """
    Retrieve, update or delete a code snippet.
    """
    try:
        tests = get_object_or_404(info, pk=pk)
    except tests.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = chatbotSerializer(tests)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = chatbotSerializer(info, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        info.delete()
        return HttpResponse(status=204)