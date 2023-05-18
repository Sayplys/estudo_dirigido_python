""" Aula 07 - relacionamento entre classes """

class Endereco:
    def __init__(self, cep, numero):
        self.cep = cep
        self.numero = numero

    def __str__(self):
        return f'Endereço[cep={self.cep}, número={self.numero}]'

class Telefone:
    def __init__(self, ddd, numero):
        self.ddd = ddd
        self.numero = numero

    def __str__(self):
        return f'Telefone[ddd={self.ddd}, numero={self.numero}]'

class Pessoa:
    def __init__(self, cpf, nome, telefone, endereco):
        self.cpf = cpf
        self.nome = nome
        self.telefone = telefone
        self.enderecos = [endereco]
        print(nome,'\n' , endereco)

    def add_endereco(self, endereco):
        print(endereco)
        self.enderecos.append(endereco)

    def __str__(self) -> str:
        return f'Pessoa[cpf={self.cpf}, nome={self.nome}, telefone{self.telefone}]'
    
pessoa1 = Pessoa('11233213', 'João da Silva', Telefone('11', '11111-1111'), Endereco('032131', '1723'))
pessoa1.add_endereco(Endereco('034341', '1432'))

pessoa2 = Pessoa('2313213', 'Lagostin', Telefone('11', '11111-1111'), Endereco('32423423', '132'))

