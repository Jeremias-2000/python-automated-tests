from bdd.steps.example_steps import Middleware
import requests



def faz_requisicao(middleware:Middleware):
    # acredito que aqui faça o enpoint e o payload
   
    #endpoint = monta_url()
    if middleware.operacao == 'GET':
        #requests.get()
        print('fez um GET')
    elif middleware.operacao == 'POST':
        #payload = monta_payload()
        #requests.post(endpoint,json=payload)
        print('fez um POST')
    elif middleware.operacao == 'PUT':
        #payload = monta_payload()
        #requests.put(endpoint,json=payload)
        print('fez um PUT')
    
def monta_url():
    pass

def monta_payload():
    pass