""" Aula 01 - Intro oo """

# paradigma de progamação

# calcular a área e o perimetro de um retangulo
# estrutura para armazenar os valores necessários para os calculos
# area = base * altura
# perimetro = 2(base + altura)

retangulo_1 = {
    'base': 10,
    'altura': 5
}

retangulo_2 = {
    'base': 6,
    'altura': 3
}

# realizar os calculos
def calcular_area(retangulo):
    return retangulo['base'] * retangulo['altura']

def calcular_perimetro(retangulo):
    return 2 * (retangulo['base'] + retangulo['altura'])

print(calcular_area(retangulo_1))
print(calcular_perimetro(retangulo_1))

print(calcular_area(retangulo_2))
print(calcular_perimetro(retangulo_2))


# Classe representa um conceito
# Classe representa um retangulo
# Classe possui atributos
# Classe possui métodos (função dentro da classe)
class Retangulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def calcular_area(self):
        return self.altura * self.base
    
    def calcular_perimetro(self):
        return 2 * (self.base + self.altura)

# Instanciando objetos do tipo Retangulo
# Chamando o método construtor
retangulo_1 = Retangulo(10, 5)
retangulo_2 = Retangulo(6, 3)

print(type(retangulo_1), retangulo_1)
print(type(retangulo_2), retangulo_2)

print(retangulo_1.base, 
      retangulo_1.altura, 
      retangulo_1.calcular_area(), 
      retangulo_1.calcular_perimetro()
      )

print(retangulo_2.base, 
      retangulo_2.altura, 
      retangulo_2.calcular_area(),
      retangulo_2.calcular_perimetro()
      )
