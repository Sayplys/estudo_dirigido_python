""" Ex 01 """

numerosInput = input("3 números: ")
numeros = numerosInput.split(',')
numeros = [int(numero) for numero in numeros]
maiorNumero = numeros[0]
menorNumero = numeros[0]


for numero in numeros:
    if numero < menorNumero:
        menorNumero = numero
    elif numero > maiorNumero:
        maiorNumero = numero

print(f"Menor número: {menorNumero}, maior número: {maiorNumero}")
