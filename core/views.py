from django.http.response import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import json
from core.utils import send_message, process_message

@csrf_exempt
def event(requests):
    try:
        json_list = json.loads(requests.body)
        chat_id = json_list['message']['chat']['id']
        command = json_list['message']['text']
        output = process_message(command)
        send_message(output, chat_id)
    except Exception as ex:
        print('erro: %s'%ex)
    return HttpResponse()

