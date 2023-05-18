""" Aula 06 - equal e hash code """

nome1 = 'jão'
nome2 = 'jão'

print(nome1 == nome2)

class Pessoa:
    def __init__(self, nome, cpf):
        self.cpf = cpf
        self.nome = nome

    def __eq__(self, value):
        if isinstance(value, self.__class__):
            return self.cpf == value.cpf
        return False
    
    def __hash__(self):
        return hash(self.cpf)
    
    def __repr__(self):
        return f'Pessoa[cpf={self.cpf},{self.nome}]'


pessoa1 = Pessoa('Jão', '342342422-x')
pessoa2 = Pessoa('Jão', '342342422-x')
pessoa3 = Pessoa('Maria', '23523535-4')

pessoas = {pessoa1, pessoa2, pessoa3}
print(pessoas)
print(pessoa1 == pessoa2)

pessoas_lista = [pessoa1, pessoa2, pessoa3]
print(pessoas_lista)

print(pessoas_lista.count(pessoa1))
