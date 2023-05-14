""" Aula 01 - introdução funções """

# Função é um bloco que realiza uma tarefa especifica
# Dividir o problema em pequenas partes
# Evita duplicação de código

# 1. Standard Library Function - Built-in function
# ex: print, len

print('olá', 123, True)

nomes = ['Joçao', 'Maria']
tamanho_lista = len(nomes)
print(nomes, tamanho_lista)

# 2. User Defined Function
# Definidas pelo desenvolvedore
# Fazerem parte da solução do problema

# declaração
# nome: saudações
# parametro: nenhum
# retorno: nenhum
def saudacoes():
    print('Olá')

# Chamada
saudacoes()
saudacoes()


# declaração
# nome: saudações
# parametro: nome
# retorno: nenhum
def saudacoes(nome):
    print(f'Olá {nome}')

# Chamada
# Valores, variaves, expressoes => argumentos
# 'Maria é um argumento passado para o parâmetro nome
saudacoes('Maria')
nome = 'carlos'
saudacoes(nome)


# declaração
# nome: calcular media
# parametro: nota1, nota2, nota3
# retorno: nenhum
def calcular_media(nota1, nota2, nota3):
    media = (nota1 + nota2 + nota3) / 3
    print(media)

# Chamada
calcular_media(10, 3, 6)
n1 = 1
n2 = 10
n3 = 5.3
calcular_media(n1, n2, n3)


# declaração
# nome: calcular_media
# parametro: nota1, nota2, nota3
# retorno: media
def calcular_media(nota1, nota2, nota3):
    media = (nota1 + nota2 + nota3) / 3
    return media

media = calcular_media(10, 8, 5)
print('Valor da média', media)
