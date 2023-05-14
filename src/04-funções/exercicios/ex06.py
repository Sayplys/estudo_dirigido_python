""" Ex.06 """

def calcular_volume(*args):
    volume = 1
    for arg in args:
        volume *= (arg / 10)
    return volume

def calcular_potencia(volume, temperatura_desejada, temperatura_ambiente):
    return  volume * 0.05 * (temperatura_desejada - temperatura_ambiente)

def calcular_filtragem(volume):
    return volume * 2 

tamanhosInput = input('Comprimento, altura, largura: ')
tamanhosInput = tamanhosInput.split(',')
tamanhos = [float(tamanho) for tamanho in tamanhosInput]
volume = calcular_volume(*tamanhos)

temperaturasInput = input('Tempretura desejada, temperatura ambiente: ')
temperaturasInput = temperaturasInput.split(',')
temperaturas = [float(tamanho) for tamanho in temperaturasInput]

print(volume)
print(calcular_potencia(volume, *temperaturas))
print(calcular_filtragem(volume))