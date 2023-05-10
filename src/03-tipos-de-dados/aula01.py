""" Aula 01 - listas """

# lista
# ordenadas
# mutáveis
# indexáveis

nomes = ['ASds', 'asdfasf', "asdf"]
print(nomes, type(nomes))

# acessar elementos
print(nomes[0])
print(nomes[0:2])
print(nomes[:2])
print(nomes[1:])

# modificar elementos
nomes[0] = 'Maria'
nomes[1:] = ['Pedro', 'João']
print(nomes)

# tamanho de uma lista
# função len
print(len(nomes))

# adicionar elementos na lista
# método append
nomes.append('Marta Gomes')
print(nomes)

# métodos insert
nomes.insert(0, 'lambreta')
print(nomes)

# método extend
nomes2 = ['Kaio', 'Carlos']
nomes.extend(nomes2)
print(nomes)

# remover elemento
# remove

nomes.remove('Maria')
print(nomes)

#del
del nomes[2]
print(nomes)

# remove da memória
# del nomes

# nomes.clear()
print(nomes)

# iteração em lista
for nome in nomes:
    print(nome)

print('----')

for i in range(len(nomes)):
    print(nomes[1])