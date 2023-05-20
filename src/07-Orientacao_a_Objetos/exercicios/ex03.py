""" Ex . 3 """

class Participacao:
    def __init__(self, codigo, data_inicio, data_fim, aluno):
        self.codigo = codigo
        self.data_inicio = data_inicio
        self.data_fim = data_fim
        self.aluno = aluno
        self.projeto = []

    def __eq__(self,value):
        if isinstance(value, self.__class__):
            return value.codigo == self.codigo
        return False

    def __hash__(self):
        return self.codigo

    def __str__(self):
        participante_infos = {
            'codigo' : self.codigo,
            'data de inicio': self.data_inicio, 
            'data de fim': self.data_fim,
            'aluno': self.aluno,
            'projeto': self.projeto
        }
        return f'{participante_infos}'
    
    def add_projeto(self, projeto):
        self.projeto.append(projeto)
