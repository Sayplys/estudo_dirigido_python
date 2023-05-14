""" Ex. 4 """

def soma(*args):
    soma = 0
    for arg in args:
        soma += arg
    return soma

print(soma(1,2,3))