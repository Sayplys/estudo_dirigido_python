""" Aula 08 - herança """

class Pessoa:
    def __init__(self,nome,sobrenome, cpf):
        self.nome = nome
        self.sobrenome = sobrenome
        self.cpf = cpf

    def obtem_nome_completo(self):
        return f'{self.nome} {self.sobrenome}'
    
class Cliente(Pessoa):
    def __init__(self, nome, sobrenome, cpf):
        super().__init__(nome, sobrenome, cpf)
        self.compras = []

class Funcionario(Pessoa):
    def __init__(self, nome, sobrenome, cpf, salario):
        super().__init__(nome, sobrenome, cpf)
        self.salario = salario

    def calcular_pagamento(self):
        return self.salario - ((10/100) * self.salario)

class Progamador(Funcionario):
    def __init__(self, nome, sobrenome, cpf, salario, bonus):
        super().__init__(nome, sobrenome, cpf, salario)
        self.bonus = bonus
    
    def calcular_pagamento(self):
        pagamento =  super().calcular_pagamento()
        return pagamento + self.bonus

cliente = Cliente('Paula', 'MAKSJ', '1212312312')
funcionario = Funcionario('Thiago', 'loasf', '12343124', 1234.2)
progamador = Progamador('ROlandin', 'Larga', '1254234', 1234.2, 100)

print(cliente.obtem_nome_completo())
print(funcionario.obtem_nome_completo(), funcionario.calcular_pagamento())
print(progamador.obtem_nome_completo(), progamador.calcular_pagamento())
