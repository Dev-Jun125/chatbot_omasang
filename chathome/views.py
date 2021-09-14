from django.http import HttpResponseRedirect
from django.shortcuts import render, resolve_url
from numpy import append

from chathome.models import chat
from chatting.views import basic_Conversation


def chathome(request):
    basic_Conversation
    temp = request.POST.get('chat-message-input')
    print(temp)
    print(request)
    context = {'message1': temp}
    return render(request, 'chathome/chathome.html', context)




