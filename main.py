import os
from adicionar_Pessoa import adicionar_Pessoas
from adicionar_pessoas_agenda import adicionar_pessoas_agenda
from mostrar_agenda import mostrar_agenda
from criar_agenda import criar_agenda
from Pessoa import *
from menu import *
def main():
    Menu(cursor)
if __name__ == "__main__":

    print(os.getcwd())
    lista_dir = os.listdir()

    if 'agendas' not in lista_dir:
      os.mkdir('./agendas')  

    cursor = ''
    while(cursor != '6'):
        print(' Menu agenda:')
        print('Digite o número correspondente à operação desejada')
        print('1 - Criar agenda')
        print('2 - Adicionar pessoas à agenda')
        print('3 - Listar todas as pessoas da agenda')
        print('4 - Listar pessoa específica da agenda')
        print('5 - Deletar agenda')
        print('6 - Encerrar programa')
        cursor = str(input())
        if (cursor.isdigit()) and (cursor >'0') and (cursor < '7'):
            main()
        else:
            print('entrada inválida\n*******************************\n')