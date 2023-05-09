""" EX - 2 """

notas = input("Notas(formato 'n1, n2, n3, nx'):")
total = 0
notas = notas.split(',')
notas = [float(nota) for nota in notas] 
for nota in notas:
    total += nota

media = total / len(notas)

print(f'media: {media}')

if media > 10:
    print("Inválido")
if media > 6:
    print("Aprovado")
elif media > 4:
    print("Recuperação")
elif media > 0:
    print("reprovado")
else:
    print("Inválido")
