""" Aula 5 - Debug pdb"""

def somar(n1, n2, n3):
    soma = n1 + n2 + n3
    return soma

def calcular_media(n1, n2, n3):
    soma = somar(n1, n2, n3)
    media = soma / 3
    return media

breakpoint()
nota1 = 10
nota2 = 3
nota3 = 5.5

media = calcular_media(nota1, nota2, nota3)
