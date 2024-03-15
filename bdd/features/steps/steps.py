from behave import given,when,then
from map import test


massaSelecionada = ''

@given('seleciono a massa {massa}')
def step_seleciono_a_massa(context,massa):
    global massaSelecionada
    massaSelecionada = massa
    print(f'to usando a massa {massa}')
    


@when('executo um {metodoHttp} com a informação do cenario {cenario}')
def step_executo_um_post_com_a_informacao_do_cenario(context,metodoHttp,cenario):
        print(f'estou com a massa {massaSelecionada} e o cenario {cenario}')
        testando = test.ler_csv_cenario(massaSelecionada,cenario)
        print(f'sera se deu certo ? {testando}')


@then('o sistema me traz a listagem de alunos')
def step_o_sistema_me_traz_a_listagem_de_alunos(context):
        pass
