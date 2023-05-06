"""" Aula 06 - cOnverção de Tipos """

# Conversão de tipo implícita e explícita

leitura = 5.345
peso = 3
total = leitura * peso

# Conversão explícita (type casting)
soma = 13.4 + float('3.5')
print(soma, type(soma))

idade = int('32')
print(idade, type(idade))

nome = "Loa"
altura = 1.70

# mensagem = nome + ' tem a aultura de ' + str(altura)
mensagem = f'{nome} tem a ultura de {altura}'
print(mensagem)