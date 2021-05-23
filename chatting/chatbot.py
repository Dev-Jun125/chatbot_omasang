'''
from . import dbconnect
from . import comparison
from . import urls
from . import views
dbconnect = dbconnect.SqlCommunication()

def basic_Conversation(request):
    user_input = ''
    chatbot_respond = ''
    user_input = request
    print("나 : ",end='')
    
    print("AI : ",end='')
    response = comparison.response_select(user_input)
    print(response)
    return (response)

basic_Conversation()
'''