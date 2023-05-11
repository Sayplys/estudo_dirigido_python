""" Aula 3 - set """

# set (conjunto)
# não ordenadas
# mutáveis
# não indexáveis
# não aceitam elementos duplicados

# criação de set
numeros = {10, 5, 7, 4, 90, 3, 1}
print(numeros, type(numeros))

for numero in numeros:
    print(numero)

print(3 in numeros)
print(50 in numeros)

# adicionar itens no set
print(numeros)
numeros.add(8)
print(numeros)

# adicionar elementos de um set em outro
numeros2 = {1, 5 ,4, 100, 3, 9}
numeros.update(numeros2)
print(numeros, type(numeros))
