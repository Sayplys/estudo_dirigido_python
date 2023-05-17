""" Ex. 01 """

def carregar_dados_alunos(arquivo):
    dados = []
    for linha in arquivo.readlines():
        linha = linha.strip()
        dados.append(linha.split(','))
    
    dados_dos_alunos = []
    for dado in dados:
        dados_dos_alunos += [{'prontuario': dado[0], 'nome': dado[1], 'email': dado[2]}]

    return tuple(dados_dos_alunos)

with  open("src/06-Arquivos/exercicios/dados_dos_alunos.txt", "r", encoding="UTF-8") as dados_dos_alunos_file:
    print(carregar_dados_alunos(dados_dos_alunos_file))


