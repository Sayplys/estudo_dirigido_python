""" Ex.3 """

def linha_para_dict(arquivo, chaves):
    dados = (arquivo.readline()).split(',')
     
    dicionario = {
        chaves[0]: dados[0],
        chaves[1]: dados[1],
        chaves[2]: dados[2]
    }

    return dicionario

with open("src/06-Arquivos/exercicios/linha_com_dados.txt", 'r', encoding='UTF-8') as linha_com_dados:
    lista = input("Chaves: ").split(',')
    print(linha_para_dict(linha_com_dados, lista))
