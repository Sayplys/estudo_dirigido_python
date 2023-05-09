""" EX - 3 """

id = input("Identificador: ")

temBR = (id[0] == 'B' and id[1] == 'R')
temX = id[-1] == 'X'
temNumero = False

if(len(id) == 7 and temBR and temX):
    for x in range(2, len(id) - 1):
        if temNumero is False and '0' <= id[x] <= '9' and id[x] != '0':
            temNumero = True
        elif '0' > id[x] > '9':
            break

if temBR and temX and temNumero:
    print("Válido")
else:
    print("Inválido")