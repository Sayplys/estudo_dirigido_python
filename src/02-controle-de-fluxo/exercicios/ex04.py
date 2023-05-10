""" EX - 4 """

id = input("Identificador: ")
errorList = []

temBR = (id[0] == 'B' and id[1] == 'R')
temX = id[-1] == 'X'
temNumero = False

if(len(id)):
    for x in range(2, len(id) - 1):
        if temNumero == False and '0' <= id[x] <= '9' and id[x] != '0':
            temNumero = True
        elif '0' > id[x] > '9':
            break
        
if temBR == False:
    errorList.append("O identificador não inicia com a sequências BR")
if temNumero == False:
    errorList.append("O identificador não apresenta números inteiros entre 0001 e 9999")
if temX == False:
    errorList.append("O identificadorr não finaliza com o caracter X")


if temBR and temX and temNumero:
    print("Válido")
else:
    print(f"Identificador informado: {id}")
    print("     Erros:")
    for x in range(len(errorList)):
        print(f'        {errorList[x]}')
