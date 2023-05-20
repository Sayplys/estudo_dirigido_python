""" Ex.02 """

from ex03 import linha_para_dict

def carregar_dados_projetos(arquivo):
    dados_dos_projetos = []
    chaves = ['codigo','titulo','responsavel']
    for linha in arquivo.readlines():
        dados_dos_projetos.append(linha_para_dict(linha.strip(), chaves))

    return tuple(dados_dos_projetos)

with open('src/06-arquivos/exercicios/dados_dos_projetos.txt', 'r', encoding='UTF-8') as dados_dos_projetos_file:
    print(carregar_dados_projetos(dados_dos_projetos_file))
