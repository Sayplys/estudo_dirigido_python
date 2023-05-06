"""" Aula 2 - Keyword e identificadores """

# Palavras resevadas
# True, False, None, and, import, lambda

# Identificadores 
# Nome de váriaveis, funçoes, classes
# Case sensitive
# Iniciam com uma letra ou _
# Não podem ter espaço em branco
# Não pode usar caracteres especiais !, @, #, $

NOME = "eu"
IDADE = 20

NOME.upper()

# Boas práticas (clean code)

C = 10
CONTADOR = 10

S = C + CONTADOR
SOMA = C + CONTADOR

# Constantes

PI = 3.14

idade = 18
MAIORIDADE = 18
if idade >= MAIORIDADE:
    print('Maior de idade')
else:
    print('Menor de idade')