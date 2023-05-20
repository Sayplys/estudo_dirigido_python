""" Ex 01 """

class Aluno:
    def __init__(self, prontuario, nome, email):
        self.prontuario = prontuario
        self.nome = nome
        self.email = email
    
    @property
    def prontuario(self):
        return self._prontuario

    @prontuario.setter
    def prontuario(self, value):
        if value == '':
            raise ValueError("Sem informações do prontuario")
        self._prontuario = value

    def __str__(self):
        return f'Aluno: {self.nome}, prontuario: {self.prontuario}, email: {self.email}'

    def __repr__(self):
        return f'{self.prontuario} + {self.nome} + {self.email}'
    
    def __eq__(self, value):
        if isinstance(value, self.__class__):
            return self.prontuario == value.prontuario
        return False
    
    def __hash__(self):
        return self.prontuario
    
aluno = Aluno('13434', 'pedro da silva', 'pedro@gmail.com')
aluno1 = Aluno('2345245', 'pedro', 'pedro@gmail.com')
aluno2 = Aluno('523452', 'adfadf', 'afdsj@gmail.com')

print(aluno)
