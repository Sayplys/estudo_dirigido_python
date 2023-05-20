""" Ex . 3 """

class Participação:
    def __init__(self, codigo, data_inicio, data_fim, aluno, projeto):
        self.codigo = codigo
        self.data_inicio = data_inicio
        self.data_fim = data_fim
        self.aluno = aluno
        self.projeto = projeto

    def __eq__(self,value):
        if isinstance(value, self.__class__):
            return value.codigo == self.codigo
        return False

    def __hash__(self):
        return self.codigo

    def __str__(self):
        participante_infos = (
            self.codigo, 
            self.data_inicio, 
            self.data_fim,
            self.aluno,
            self.projeto
        )
        return f'{participante_infos}'

participante = Participação('34132', '05/02', '05/12', 'paula', 'aula')

print(participante)
