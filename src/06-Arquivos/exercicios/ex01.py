""" Ex. 01 """

from ex03 import linha_para_dict

def carregar_dados_alunos(arquivo):
    dados_dos_alunos = []
    chaves = ['prontuario', 'nome', 'email']
    for linha in arquivo.readlines():
        dados_dos_alunos.append(linha_para_dict(linha.strip(),chaves))

    return tuple(dados_dos_alunos)

with  open("src/06-Arquivos/exercicios/dados_dos_alunos.txt", "r", encoding="UTF-8") as dados_dos_alunos_file:
    print(carregar_dados_alunos(dados_dos_alunos_file))


