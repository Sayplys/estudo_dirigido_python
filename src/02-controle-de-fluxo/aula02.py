""" Aula 02 - if """

# if condição:
#     instrução
#     instrução
#     instrução

desconto = 10
DESCONTO_ESPECIAL = desconto >= 20

if DESCONTO_ESPECIAL:
    print('Desconto especial')
else:
    print('Sem desconto especial')


# nome tem que ter pelo menos 3 caracteres
nome = "Lo"

print(len(nome), type(len(nome)))

NOME_INVALIDO = len(nome) < 3 
if NOME_INVALIDO:
    print('Nome com no mínimo 3 caracteres')
else:
    print('Nome valido')

# nome tem que ter pelo menos 3 caracteres
# idade tem que ser maior ou igual a 18
# exibir todos os erros no final apenas
nome = 'Lo'
idade = 17
erros = []

NOME_INVALIDO = len(nome) < 3
if NOME_INVALIDO:
    erros.append('Nome deve ter pelo menos 3 caracteres')

IDADE_INVALIDA = idade <= 18
if IDADE_INVALIDA:
    erros.append('Idade deve ser maior ou igual a 18')

# false : false, None, 0, 0.0, '', lista, tulpe ou set vazio
# true: todo o resto
if erros:
    print(erros)
else:
    print('Dados válidos')

# if alif else

# Verifica se um número é positivo ou negativo ou zero
numero = 3
if numero > 0:
    print('Maior que zero')
elif numero == 0:
    print('0')
else:
    print('Menor que zero')

# calcule a média e verifique se as duas notas
# são válidas antes do cálculo
n1 = 5.6
n2 = 10

if (0 <= n1 <= 10 and 0 <= n2 <= 10):
    media = (n1 + n2) / 2
    if media >= 6:
        print('Aprovado')
    elif media >= 4:
        print('Recuperação')
    else:
        print('Reprovado')
else:
    print('nota inválida')