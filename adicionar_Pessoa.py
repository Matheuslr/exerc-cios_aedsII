from Pessoa import *

def _preencher_nome():
    nome = ''
    while(nome is ''):
        print('Digite o nome do contato: ')
        nome = input()
    return nome
    
def _preenher_telefone():
    telefone = ''
    while(telefone is ''):
        print('Digite o telefone do contato: ')
        telefone = input()
        if not (telefone.isdigit()):
            print('Digite apenas números!\n')
            telefone = ''
    return telefone

def _preencher_email():
    email = ''
    while(email is ''):
        print('Digite o email do contato: ')
        email = input()
    return email

def _validacao(validador):
    input_saida = ''
    while(input_saida is ''):
        print('deseja adicionar outra Pessoa?[s/n]')
        input_saida = str(input()).upper()
        deseja_continuar = (input_saida == 'S')
        deseja_sair = (input_saida == 'N')
        if(deseja_continuar or deseja_sair):
            if(input_saida == 'S'):
                validador = 'S'
                return (validador)
            else: 
                validador = 'N'
                return (validador)
        else:
            input_saida = ''
        
def adicionar_Pessoas():
    validador = 'S'
    agenda = []
    while(validador == 'S'):
        input_saida = ''
        nome = _preencher_nome()
        telefone = _preenher_telefone()
        email = _preencher_email()
        p1 = Pessoa(nome, telefone, email)
        agenda.append(p1)
        validador = _validacao(validador)
        print(validador)
    return(agenda)