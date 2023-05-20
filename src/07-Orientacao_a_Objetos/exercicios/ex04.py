""" Ex. 4 """

from ex02 import Projeto
from ex03 import Participacao
    
participante1 =  Participacao('34132', '05/02', '05/12', 'paula')
participante2 = Participacao('2312', '02/03', '02/01', 'maria')

projeto1 = Projeto('123123','aula','thiago')
projeto2 = Projeto('134232', 'crescer', 'leila')

def add_participante_ao_projeto(projeto, participante):
    projeto.add_participacao(participante)
    participante.add_projeto(projeto)

add_participante_ao_projeto(projeto1, participante2)
add_participante_ao_projeto(projeto2, participante1)


print(projeto1, '\n', projeto2)
