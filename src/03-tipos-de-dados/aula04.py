""" Aula 04 - dicionario """

# dicionário
# coleção de key-value
# key unica
# mutável


# criar um dicionário
pessoa = {
    "nome": "Pessoa",
    "idade": 18,
    "altura": 1.74,
    "peso": 60
}
print(pessoa, type(pessoa))

# acessar valor por chave
print(pessoa['nome'])
print(pessoa.get("nome"))

# pegar todas as chave, valores, pares
print(pessoa.keys())
print(pessoa.values())
print(pessoa.items())

# verifica se a chave existe
print("olho" in pessoa)

# adicionar chave/valor de forma dinâmica
pessoa["olho"] = "azul"
print("olho" in pessoa)
print(pessoa)

# remove a chave
olho = pessoa.pop("olho")
print(pessoa)
print(olho)

# loop
for key in pessoa:
    print(key, pessoa[key], type(key))

for value in pessoa.values():
    print(value)

for key in pessoa.keys():
    print(key)

print(pessoa.items())

for key, value in pessoa.items():
    print(key, value)

# lista de dicionarios

aluno1 = {
    'nome': 'joão',
    'email': 'joão@gmail.com',
    'notas': [1, 2, 3, 4]
}

aluno2 = {
    'nome': 'maria',
    'email': 'maria@gmail.com',
    'notas': [1, 2, 3, 4]
}

alunos = [aluno1, aluno2]

for aluno in alunos:
    print(aluno['nome'], aluno['email'])
    for nota in aluno['notas']:
            print(nota)