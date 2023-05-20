""" Ex. 01 """

import moeda

numero = int(input('Informe número: '))
print(f'Adicionar = {moeda.aumentar(numero, 100)}, Diminuir = {moeda.diminuir(numero, 100)}')
print(f'dobrar = {moeda.dobro(numero)}, metade = {moeda.metade(numero)}')
