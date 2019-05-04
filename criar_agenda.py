from Pessoa import *
import os
def criar_agenda(agenda,nome_agenda):

    caminho_agenda = './agendas/' + nome_agenda + '.txt'

    with open(caminho_agenda, 'w+') as file:
        for individuo in agenda:
            p1 = Pessoa()
            p1 = individuo
            p1_dict = p1.Pessoa_to_dict()
            file.write(str(p1_dict))
