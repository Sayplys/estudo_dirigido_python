""" Ex. 4 """

class Projeto:
    def __init__(self, codigo, titulo, responsavel):
        self.codigo = codigo
        self.titulo = titulo
        self.responsavel = responsavel
        self.participacoes = []
    
    @property
    def codigo(self):
        return self._codigo
    
    @codigo.setter
    def codigo(self, value):
        if value == '':
            raise ValueError('Sem informação do codigo')
        self._codigo = value 

    @property
    def titulo(self):
        return self._titulo
    
    @titulo.setter
    def titulo(self, value):
        if value == '':
            raise ValueError('Sem informação do titulo')
        self._titulo = value 

    @property
    def responsavel(self):
        return self._responsavel
    
    @responsavel.setter
    def responsavel(self, value):
        if value == '':
            raise ValueError('Sem informação do responsavel')
        self._responsavel = value 

    def __str__(self):
        return f'codigo={self.codigo},\ntitulo={self.titulo},\nresponsável={self.responsavel},\nparticipação={self.participacoes}'

    def __repr__(self):
        return f'{self.codigo},{self.titulo},{self.responsavel}'

    def __eq__(self,value):
        if isinstance(value, self.__class__):
            return self.codigo == value.codigo
        return False
    
    def __hash__(self):
        return self.codigo

    def add_participacao(self, participacao):
        self.participacoes.append(participacao)

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
    
participante1 =  Participação('34132', '05/02', '05/12', 'paula', 'aula')
participante2 = Participação('2312', '02/03', '02/01', 'maria', 'aluno')

projeto1 = Projeto('123123','aula','thiago')
projeto1.add_participacao(participante1)
projeto1.add_participacao(participante2)

print(projeto1)
