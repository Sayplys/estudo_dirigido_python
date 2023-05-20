""" Aula 01 - Modulos e pacotes """

# import ulteis
from ulteis import numeros

num = int(input("Digite valor: "))
fat = numeros.fatorial(num)
print(f'0 fatorial de {num} é {fat}')
print(f'O dobro é {numeros.dobro(num)}')
