""" Ex.3 """

def linha_para_dict(linha, chaves):
    dados = linha.split(',')
     
    dicionario = {
        chaves[0]: dados[0],
        chaves[1]: dados[1],
        chaves[2]: dados[2]
    }

    return dicionario
