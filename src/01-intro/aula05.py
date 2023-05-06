""" Aula 05 - Tipos de dados """

# Númericos
# int, float

idade = 20
peso = 70.5

print(idade, type(idade))
print(peso, type(peso))

# String
nome = 'João'
sobrenome = 'dos Santos'
nome_completo = nome + '' + sobrenome
print(nome_completo)

produto = 'Coca-cola'

# O cliente nome_completo comprou o produto 
print(f'O cliente {nome} {sobrenome} comprou o produto {produto}')

print(nome[0], nome[-1])

print(nome.find('o'))

# Boolean
ligado = True
print(ligado, type(ligado))

resultado = 10 == 10
print(resultado, type(resultado))

# Listas
frutas = ['banana', 'uva', 'morango']
print(frutas)
print(frutas[0])
print(frutas[1])

frutas[0] = 'banana nanica'
frutas.append('abacaxi')
print(frutas)
print(len(frutas))

for fruta in frutas:
        print(fruta.upper())

# Tupla
codigos = ('SP01', 'SP02')
print(codigos[0])

# codigos[0] = 'SP05' # TypeError
print(len(codigos))

# Conjuntos
resultados_sorteio = {10, 4, 3, 55, 9}
print(resultados_sorteio)

resultados_sorteio.add(23)
print(resultados_sorteio)

# Dicionário

funcionario = {
        'codigo': 213,
        'nome': 'poef fdkja', 
        'salario': 2323
}

print(funcionario)
print(funcionario['codigo'])

print(funcionario.keys())

funcionario['salario'] = 3432.00
print(funcionario)