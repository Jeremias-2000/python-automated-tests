from behave import given,when,then
from map.test import ler_csv_cenario


class Middleware: #POST,/test,test.csv,{'message':'ok'}
        def __init__(self,operacao:str= '',endpoint:str= '',massa:str= '',leitura_csv:dict={},response:dict={}) -> None:
               self.operacao = operacao
               self.endpoint = endpoint
               self.massa = massa
               self.leitura_csv = leitura_csv
               self.response = response
               
        #@property
        
        
interceptor = Middleware()


@given('seleciono a massa {massa}')
def step_seleciono_a_massa(context,massa):
    interceptor.massa = massa.replace('"', '')
    print(f'to usando a massa {massa}')
    


@when('executo um {metodoHttp} com a informação do cenario {cenario}')
def step_executo_um_post_com_a_informacao_do_cenario(context,metodoHttp,cenario):
        print(f'estou com a massa {interceptor.massa} e o cenario {cenario}')
        interceptor.operacao = metodoHttp.replace('"', '')
        interceptor.leitura_csv = ler_csv_cenario(interceptor.massa,cenario)
       


@then('o sistema me traz a listagem de alunos')
def step_o_sistema_me_traz_a_listagem_de_alunos(context):
        from request.test import faz_requisicao
        faz_requisicao(middleware=interceptor)
        