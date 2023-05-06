"""" Aula 07 - entrada e saida """

# saída padrão - sys stdout
print('Hello world' , 'pessoa')

print('aaaa', 'bbbbb', 32, True, sep='---', end='////\n')
print('aaaa', 'bbbbb', 32, True, sep='///', end='\n')

arquivo = open('nsdfijasd.txt', 'w', encoding='utf-8')
print('jão', 'pessoa', 'sjdf', file=arquivo, sep=';')

# Entrada
nome = input('Digite seu nome: ')
idade = int(input('Digite dua idade: '))
print(type(nome), type(idade))

if idade >=18:
    print(f'{nome}, você é maior de idade')
else:
    print(f'{nome}, você é menor de idade')

# file
arquivo_notas = open('notas.txt', 'r', encoding='utf-8')

conteudo = arquivo_notas.read()
notas = conteudo.split(sep=';')
notas = [float(nota) for nota in notas]

media = (notas[0] + notas[1] + notas[2]) / 3
print(media)