""" Ex.02 """

def carregar_dados_projetos(arquivo):
    dados = []
    for linha in arquivo.readlines():
        linha = linha.strip()
        dados.append(linha.split(','))

    dados_dos_projetos = []
    for dado in dados:
        dados_dos_projetos.append({'código': dado[0], 'titulo': dado[1], 'responsável': dado[2]})

    return tuple(dados_dos_projetos)

with open('src/06-arquivos/exercicios/dados_dos_projetos.txt', 'r', encoding='UTF-8') as dados_dos_projetos_file:
    print(carregar_dados_projetos(dados_dos_projetos_file))
