import os
from Pessoa import *
def _arquivo_no_diretorio(nome_agenda):
    lista_arquivos = os.listdir('./agendas')
    nome_arquivo_agenda = nome_agenda + '.txt'
    if nome_arquivo_agenda in lista_arquivos:
        return True
    else:
        return False

def lista_agenda():
    print('Agendas disponíveis')
    lista_arquivos = os.listdir('./agendas')
    for elemento in lista_arquivos:
        print(elemento.replace(".txt", ""))

def _recuperar_lista_pessoas(nome_agenda):
    caminho_agenda = './agendas/' + nome_agenda + '.txt'
    lista_pessoas = []
    lista_agenda = []
    with open(caminho_agenda, 'r') as file :
        lista_pessoas = file.readline().split("{")
        del lista_pessoas[0]
    for pessoa in lista_pessoas:
        pessoa = '{' + pessoa
        pessoa = (eval(pessoa))
        nome = pessoa['nome']
        telefone = pessoa['telefone']
        email = pessoa['email']
        p1 = Pessoa(nome, telefone, email)
        lista_agenda.append(p1)
    return(lista_agenda)

def mostrar_agenda(nome_agenda, procurar_nome = None):

    arquivo_diretorio = _arquivo_no_diretorio(nome_agenda)    
    if arquivo_diretorio:
        lista_agenda = _recuperar_lista_pessoas(nome_agenda)
        if procurar_nome:
            contador = 0
            for individuo in lista_agenda:
                if individuo.nome == procurar_nome:
                    print('**************************************************')
                    individuo.Pessoa_to_string()
                    contador += 1
                    print('**************************************************')
            if contador == 0: 
                print('Nome não existe na agenda')
        else:
            for individuo in lista_agenda:
                print('**************************************************')
                individuo.Pessoa_to_string()
                print('**************************************************')
    else:
        print('Agenda não existe')             
