""" Ex.02 """

def carregar_dados_projetos(arquivo):
    dados = []
    for linha in arquivo.readlines():
        linha = linha.strip()
        dados.append(linha.split(','))

    lista_de_dados_do_projeto = []
    for dado in dados:
        lista_de_dados_do_projeto.append({'código': dado[0], 'titulo': dado[1], 'responsável': dado[2]})

    dados_de_projeto = tuple(lista_de_dados_do_projeto)
    return dados_de_projeto

with open('src/06-arquivos/exercicios/dados_dos_projetos.txt', 'r', encoding='UTF-8') as dados_dos_projetos_file:
    print(carregar_dados_projetos(dados_dos_projetos_file))
