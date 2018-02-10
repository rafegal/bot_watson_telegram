from core.constants import TOKEN_CLIMA_TEMPO, USER_NAME_WATSON, PASSWORD_WATSON, VERSION_WATSON, TOKEN_TELEGRAM, WORKSPACE_WATSON
import requests
from watson_developer_cloud import ConversationV1
import json


def process_message(text):
    conversation = ConversationV1(
        username=USER_NAME_WATSON,
        password=PASSWORD_WATSON,
        version=VERSION_WATSON)

    response = conversation.message(workspace_id=WORKSPACE_WATSON, input={
        'text': text})
    output = response.get('output')
    text_output = output.get('text')[0]
    action = output.get('action')
    print(response)
    if action == 'clima':
        response = requests.get('http://apiadvisor.climatempo.com.br/api/v1/forecast/locale/3477/days/15?token={0}'.format(TOKEN_CLIMA_TEMPO))
        text_output += '\n' + json.loads(response.text)['data'][0]['text_icon']['text']['phrase']['reduced']
    print(text_output)
    return text_output


def send_message(text, chat_id):
    url = 'https://api.telegram.org/bot{}/sendMessage'.format(TOKEN_TELEGRAM)
    data = {'chat_id':chat_id, 'text':text}
    response = requests.post(url, data=data)
