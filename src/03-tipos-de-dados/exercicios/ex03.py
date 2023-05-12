""" ex 03 """

mes_numerico_input = input("Mês em formato númerico: ")
mes_numerico = int(mes_numerico_input)

meses = {1 : 'Janeiro', 2: 'Fevereiro', 3: 'Março', 4: 'Abril', 5: 'Maio',
          6: 'Junho', 7: 'Julho', 8: 'Agosto', 9: 'Setembro', 
          10: 'Outubro', 11: 'Novembro', 12: 'Dezembro'}

print(meses.get(mes_numerico))
