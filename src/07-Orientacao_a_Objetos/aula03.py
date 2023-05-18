""" Aula 03 - métodos de classe """

class Retangulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    @classmethod
    def criar_pela_lista(cls, lista):
        return cls(lista[0], lista[1])

    @classmethod
    def from_string(cls, rep_retangulo):
        base, altura = rep_retangulo.split(sep=',')
        return cls(float(base), float(altura))

    def calcular_area(self):
        return self.altura * self.base
    
    def calcular_perimetro(self):
        return 2 * (self.base + self.altura)

retangulo1 = Retangulo(10, 5)
retangulo2 = Retangulo(6, 3)
retangulo3 = Retangulo.criar_pela_lista([10, 30])
retangulo4 = Retangulo.from_string('10, 2.5')

print(retangulo3.base, retangulo3.altura, retangulo3.calcular_area())
print(retangulo4.base, retangulo4.altura, retangulo4.calcular_area())
