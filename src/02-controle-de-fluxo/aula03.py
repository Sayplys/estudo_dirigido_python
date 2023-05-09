""" Aula 03 - loop for """

# 1. Repetir instrução
# 2. Iteração em coleção de elementos

linguagens = ['c','python','java']

# for valor in coleção:
#     instrução

for linguas in linguagens:
    print(linguas)

# comportamento do operador in é
# diferente com base no contexto
print('java' in linguagens)

nota1 = 10.0
nota2 = 5.5
nota3 = 8.3

media = (nota1 + nota2 + nota3) / 3
print(media)

notas = [10.0, 5.5, 8.3]

soma = 0.0
for nota in notas:
    soma = soma + nota

media = soma / len(notas)
print(media)

# range
# valores = range(10)
# valores = range(0, 10)
# valores = range(0, 10, 2)
valores = range(0, 10, 3)
print(valores)

for valor in valores:
    print(valor)

# for i in range(len(linguagens)):
#     print(linguagens[i])
