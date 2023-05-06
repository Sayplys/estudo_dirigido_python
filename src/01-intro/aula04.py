""" Aula 4 - Variáveis, Constantes e Literais """
# Variável container para guardar dados

numero = 10
print(numero, type(numero))

# alterar o valor de uma variável
numero = 20
print(numero)

# multiplas atribuições
nome, idade, endereco = 'nome', 20, 'Rua sdsafsij'
print(nome, idade, endereco)

nome = 'nome'
idade = 20
endereco = 'Rua sfdhjafjh'
print(nome, idade, endereco)

# atribui o mesmo valor para várias variáveis
nome1 = nome2 = nome3 = 'João'
print(nome1, nome2, nome3)

nome2 = 'Pedro'
print(nome1, nome2, nome3)

# variáveis
# snake_case
id_funcionario = 23498
salario_atual = 5000
print(id_funcionario, salario_atual)

# Constantes
# Upper case - snake_case

PI = 3.14
MAIORIDADE_CIVIL = 21
MAIORIDADE_PENAL = 18

print(PI, MAIORIDADE_CIVIL, MAIORIDADE_PENAL)

# Literais

idade = 27
print(idade)
print(27)

# Númericos
print(10, type(10))
print(10.5, type(10.5))

# String
print('Maria', type('Maria'))
print("Laos", type("Laos"))

# Booleano
print(True, type(True))
print(False, type(False))

# Coleções

# Liste
numeros = [1, 3, 5]
print(numeros, type(numeros))

# Tupla (tuple)
emails = ('sdj@gmail.com', 'sadh@gmail.com')
print(emails, type(emails))

# Conjunto (set)
nomes = {'maria', 'joão', 'pedro', 'kaio'}
print(nomes, type(nomes))

# Dicionario (Dictionary)
aluno = {
    'prontuario': 1232,
    'nome': 'Nome sobrenome',
    'idade': 32
}
print(aluno, type(aluno))
