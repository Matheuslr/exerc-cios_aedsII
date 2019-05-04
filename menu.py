from adicionar_Pessoa import adicionar_Pessoas 
from adicionar_pessoas_agenda import adicionar_pessoas_agenda
from mostrar_agenda import mostrar_agenda, lista_agenda
from criar_agenda import criar_agenda
from deletar_agenda import deletar_agenda
from Pessoa import *
from main import *

def Menu(cursor):
    if cursor == '1':
        agenda = adicionar_Pessoas()
        print('\nDigite o nome da agenda:')
        nome_agenda = input()
        criar_agenda(agenda, nome_agenda)
        print('**************************************************')
    elif cursor == '2':
        agenda = adicionar_Pessoas()
        print('\nDigite o nome da agenda:')
        nome_agenda = input()
        adicionar_pessoas_agenda(agenda, nome_agenda)
        print('**************************************************')
    elif cursor == '3':
        lista_agenda()
        print('\nDigite o nome da agenda desejada')
        nome_agenda = input()
        mostrar_agenda(nome_agenda)
        print('**************************************************')

    elif cursor == '4':
        lista_agenda()
        print('\nDigite o nome da agenda desejada')
        nome_agenda = input()
        print('\nDigite o nome da pessoa a ser procurada')
        nome_pessoa = input()
        mostrar_agenda(nome_agenda, nome_pessoa)
        print('**************************************************')

    elif cursor == '5':
        lista_agenda()
        print('\nDigite o nome da agenda que você deseja deletar')
        nome_agenda = input()
        deletar_agenda(nome_agenda)
        print('**************************************************')
    
    else:
        print('programa encerrado')
