import os
from mostrar_agenda import lista_agenda

def _arquivo_no_diretorio(nome_agenda):
    lista_arquivos = os.listdir('./agendas')
    nome_arquivo_agenda = nome_agenda + '.txt'
    if nome_arquivo_agenda in lista_arquivos:
        return True
    else:
        return False

def deletar_agenda(nome_agenda): 
    arquivo_diretorio = _arquivo_no_diretorio(nome_agenda)

    if arquivo_diretorio:
        path = './agendas/' + nome_agenda + '.txt'
        os.remove(path)
    else:
        print('Agenda não existe!')