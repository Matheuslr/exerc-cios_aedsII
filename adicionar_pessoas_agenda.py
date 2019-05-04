from Pessoa import *
import os

def _arquivo_no_diretorio(nome_agenda):
    lista_arquivos = os.listdir('./agendas')
    nome_arquivo_agenda = nome_agenda + '.txt'
    if nome_arquivo_agenda in lista_arquivos:
        return True
    else:
        return False

def adicionar_pessoas_agenda(agenda,nome_agenda):

    arquivo_diretorio = _arquivo_no_diretorio(nome_agenda)

    if arquivo_diretorio:

        caminho_agenda = './agendas/' + nome_agenda + '.txt'

        with open(caminho_agenda, 'a+') as file:
            for individuo in agenda:
                p1 = Pessoa()
                p1 = individuo
                p1_dict = p1.Pessoa_to_dict()
                file.write(str(p1_dict))

    else:
        ('Agenda não existente!')