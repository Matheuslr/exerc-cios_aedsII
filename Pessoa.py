
import itertools
class Pessoa():
   
    newid = itertools.count().__next__
    def __init__(self, nome = None, telefone = None, email = None):
        self.nome = nome
        self.telefone = telefone
        self.email = email
        self.id = Pessoa.newid()
    
    def Pessoa_to_dict(self):
        dict_Pessoa = {
            'id': self.id,
            'nome': self.nome,
            'telefone': self.telefone,
            'email': self.email
        }

        return dict_Pessoa
    
    def Pessoa_to_string(self):
        print('Nome: {} \nTelefone: {} \nEmail: {}'.format(self.nome, self.telefone, self.email))