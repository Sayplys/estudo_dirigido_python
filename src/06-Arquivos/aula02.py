""" Aula 02 - arquivos """

# arq = open('src/06-Arquivos/arquivo.txt', 'w', encoding="UTF-8")
# x = ['Caio', 'João', 'Marcos']
# arq.write('Texto')
# arq.writelines(x)
# arq.close()

# context manager
# with open('src/06-Arquivos/arquivo.txt', 'a', encoding="UTF-8") as arq:
#     x = ['Caio', 'João', 'Marcos']
#     # arq.write('Texto')
#     # arq.writelines(x)
#     for nome in x:
#         arq.write(nome + '\n')

with open('src/06-Arquivos/arquivo.txt', 'r', encoding="UTF-8") as arq:
    x = arq.read()
    print(x)

