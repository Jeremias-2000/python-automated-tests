from steps.example_steps import Middleware
import os
import json
#import requests



def faz_requisicao(middleware:Middleware):
    
    endpoint = monta_url(middleware.massa)
    middleware.endpoint = endpoint
    print(endpoint)
    if middleware.operacao == 'GET':
        #requests.get()
        print('fez um GET')
    elif middleware.operacao == 'POST':
        payload = json.loads(middleware.leitura_csv['json_exemplo'])
        #payload = monta_payload()
        #requests.post(endpoint,json=payload)
        print('fez um POST')
    elif middleware.operacao == 'PUT':
        #payload = monta_payload()
        #requests.put(endpoint,json=payload)
        print('fez um PUT')
    
def monta_url(massa:str):
    endpoint = os.getenv('testando')
    if endpoint == '':
        raise Exception('env not found')
    return endpoint

def set_headers():
    #posso passar kwargs aqui e o que tiver e achar seta no map senao achar lança raiseException
    pass

    """
    headers = {
    'User-Agent': 'My User Agent',  # Example header
    'Content-Type': 'application/json',  # Example header
    'Authorization': 'Bearer YourAccessToken',  # Example header for authorization
}


response = requests.get('https://api.example.com', headers=headers)


print(response.text)
    """