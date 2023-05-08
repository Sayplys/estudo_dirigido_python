"""" Aula 01 - Operadores """

# Operadores Aritméticos

N1 = 10.2
N2 = 3.5
RESULTADO = N1 + N2 + 8.5


print('1 + 1', 1+ 1, type(1+1))
print('1.2 + 1.3', 1.2 + 1.3, type(1.2 + 1.3))
print('resultado: ', RESULTADO, type(RESULTADO))
print(3-1)
print(3*2, type(3*2))
print(3/2, type(3/2))
print(3 % 2)
print(10 // 3, type(10//3))
print(10 ** 2)

# Operador de atribuição
X = 10.0
print(X)

# Operadores de comparação
RESULTADO = X > 10
print(RESULTADO, type(RESULTADO))

print('10 == 10', 10 == 10, type(10 == 10))
print('10 != 10', 10 != 10, type(10 != 10))
print('10 > 10', 10 > 10, type(10 > 10))
print('10 >= 10', 10 >= 10, type(10 >= 10))
print('10 < 10', 10 < 10, type(10 < 10))
print('10 <= 10', 10 <= 10, type(10 <= 10))

# condicao = X > 10 and RESULTADO < 3 and X 
# if condicao:
#     pass

print('True and True, ', True and True, type(True and True))
print('True and False, ', True and False, type(True and False))
print('False and True, ', False and True, type(False and True))
print('False and False, ', False and False, type(False and False))

print('True or True, ', True or True, type(True or True))
print('True or False, ', True or False, type(True or False))
print('False or True, ', False or True, type(False or True))
print('False or False, ', False or False, type(False or False))

CONDICAO = True
print('not condição', not CONDICAO, type(not CONDICAO))

# Operadores especiais

# is
# == comparar se dois valores são iguais
# is verifica se as variáveis apontam para o mesmo objeto em memória

a = 10
b = 10.0
c = b

print(a == b, a == c, b == c)
print(a is b, a is c, b is c)

# in
# str, list, tuple, set, dic (chave)

frase = 'Tá porra maluco'
print('porra' in frase, type('porra' in frase))

numeros = {1, 5, 2, 6} # [] () {}
print(10 in numeros)

pessoa = {
    'nome' : 'pessoa',
    'idade' : 22,
    'email': 'pessoa@gmail.com'
}

print('asdgf' in pessoa)
