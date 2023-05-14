""" Aula 02 - argumentos: positional, keywords, default value """

# declara uma função que soma dois numeros
def somar(n1, n2):
    return n1 + n2

def dividir(dividendo, divisor):
    return dividendo / divisor

# argumentos posicionais
print('Somar',somar(10, 5))
print("Dividir:", dividir(10, 6))

# unpack list e tuplas
numeros = [10, 5.5]
print('Somar numeros de uma lista', somar(numeros[0], numeros[1]))
print('Somar numeros de uma lista', somar(*numeros))

# unpack dict
numeros = {
    "n1": 10.3,
    "n2": 5.34
}

print('somar numeros de um dict:', somar(**numeros))

# argumentos nomeados (keyword)
print('somar:', somar(n1=9.4, n2=7.5))
print('somar:', somar(n2=5.6, n1=7.5))
print('dividir:', dividir(divisor=10, dividendo=6))

# Declaração 
# nome: saudações
# parâmetro: nome (obragatorio), saudação (opcional)
# retorno: string
def saudacoes(nome, saudacao='Oi'):
    return f'{saudacao} {nome}'

print(saudacoes('Jõao', 'Olá'))
print(saudacoes('Maracatua'))
