""" Aula 05 - Métodos especiais """

class Retangulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def calcular_area(self):
        return self.altura * self.base
            
    def calcular_perimetro(self):
        return 2 * (self.base + self.altura)
    
    # __str__(self)
    # representação do objeto como string para humanos
    def __str__(self):
        return f'Retangulo[base={self.base}, altura={self.altura}]'
    
    # __repr__(self)
    # representação do objeto como string para recriar
    # esse objeto
    # loggin, debug
    # representação canonica
    def __repr__(self):
        return f'Retangulo({self.base},{self.altura})'


retangulo1 = Retangulo(10, 3)
retangulo2 = Retangulo(4,4)

print(retangulo1.__repr__())

retangulo3 = eval('Retangulo(7.5,12.3)')
retangulo4 = eval(repr(retangulo3))

print(retangulo1)
print(retangulo2)
print(retangulo3)
print(retangulo4)
