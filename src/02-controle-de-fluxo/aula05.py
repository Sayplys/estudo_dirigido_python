""" Aula 05 - break e continue """

for i in range(10):
    if i == 4:
        break
    print(i)

# encontrar a posição de um numero
# em uma lista de inteiros. Caso não
# enconte posição é igual a -1

numero = 5
numeros = [1, 2, 4, 8, 5, 2, 7, 9]
posicao = -1

contador = 0
for num in numeros:
    if num == numero:
        posicao = contador
        break

    contador += 1
print(posicao)

# continue
# pular a iteração atual

for numero in numeros: 
    if numero == 3:
        continue
    print(numero)
