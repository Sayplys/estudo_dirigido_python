""" Ex. 2 """

class Projeto:
    def __init__(self, codigo, titulo, responsavel):
        self.codigo = codigo
        self.titulo = titulo
        self.responsavel = responsavel
    
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
        return f'codigo={self.codigo}, titulo={self.titulo}, responsável={self.responsavel}'

    def __repr__(self):
        return f'{self.codigo},{self.titulo},{self.responsavel}'

    def __eq__(self,value):
        if isinstance(value, self.__class__):
            return self.codigo == value.codigo
        return False
    
    def __hash__(self):
        return self.codigo

projeto1 = Projeto('123123','aula','thiago')
projeto2 = Projeto('123123','nada','marilia')

print(projeto1)