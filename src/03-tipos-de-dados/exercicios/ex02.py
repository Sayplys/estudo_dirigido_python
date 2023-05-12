""" ex 02 """

mes_numerico_input = input("Mês em formato númerico: ")
mes_numerico = int(mes_numerico_input)

meses = ('Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio',
          'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro')

for mesIndex in range(0, len(meses)):
    if mesIndex == (mes_numerico - 1):
        print(meses[mesIndex])
        break
    elif mesIndex == len(meses) - 1:
        print("Mês inválido")
