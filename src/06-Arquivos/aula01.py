""" Manipulando arquivos """

# open("caminho", "r")

# Modo
# r -leitura
# a - append / incrementar
# w - escrita
# x - criar arquivo
# r+ - leitura + escrita

arquivo = open("src/06-Arquivos/test2.txt", "r", encoding="UTF-8")

# print(arquivo.readable())
# # print(arquivo.read())
# print(arquivo.readline())
# print(arquivo.readline())
# print(arquivo.readline())
# print(arquivo.readline())

# lista = arquivo.readlines()
# print(lista)

# arquivo.write('SQL\n')
# arquivo.write('Julia\n')

arquivo.close()

import os

# if os.path.exists("src/06-Arquivos/test3.txt"):
#     os.remove("src/06-Arquivos/test3.txt")
# else:
#     print('Não existe')

# os.rmdir("src/06-Arquivos/pasta")