""" Aula 02 - tupla """

# tuplas
# ordenadas
# imutáveis
# indexáveis

# criação de tupla
nomes = ('hasfha', 'asfhauiksfh', 'aufhd')
print(nomes, type(nomes))

# acessar elementos
print(nomes[0])
print(nomes [0:2])
print(nomes[:2])
print(nomes[1:])

# modificar elemento (não é possivel por ser imutável)
# nomes[0] = 'Maria'

# iteração

for nome in nomes:
    print(nome)

print('-----')

for i in range(len(nomes)):
    print(nomes[i])

nomes2 = 'ana', 'ame', 'mar'
print(nomes2, type(nomes2))

# # unpack
# nome1 = nomes2[0]
# nome2 = nomes2[1]
# nome3 = nomes2[2]
nome1, nome2, nome3 = nomes2
print(nome1, nome2, nome3)


# juntar duas tuplas
todos_nomes = nomes + nomes2
print(todos_nomes, type(todos_nomes))
