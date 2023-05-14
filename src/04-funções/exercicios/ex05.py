""" Ex. 5 """

def calculadora_IMC(**kwargs):
    peso = kwargs.get('peso')
    altura = kwargs.get('altura')
    return peso / (altura * altura)


def classificar(imc):
    classificacao = None
    if imc < 18.5:
        classificacao = 'Baixo peso'
    elif imc <= 24.9:
        classificacao = 'Peso normal'
    elif imc <= 29.9:
        classificacao = 'Excesso de peso'
    elif imc <= 34.9:
        classificacao = 'Obesidade de Classe 1'
    elif imc <= 39.9:
        classificacao = 'Obesidade de Classe 2'
    elif imc >= 40:
        classificacao = 'Obesidade de Classe 3'
    return classificacao

def situar(imc):
    if imc < 18.5:
        return 'Precisa ganhar peso'
    elif imc > 24.9:
        return 'Precisa perder peso'
    else:
        return 'Peso normal'

peso = float(input('Informe peso: '))
altura = float(input('Informe altura: '))

individuo = {
    'altura': altura,
    'peso': peso
}
imc = calculadora_IMC(peso = individuo['peso'], altura = individuo['altura'])

print('Imc:', imc)
print('Classificação: ', classificar(imc))
print('Situação: ', situar(imc))
