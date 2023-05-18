""" Aula 04 - Propiedades """

# Forma de controlar acesso aos atributos de uma instância
# formas personalisadas de obter e altera um valor de um atributo

class Retangulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    #getter
    @property
    def base(self):
        return self._base
    
    # setter
    @base.setter 
    def base(self, value):
        if value <= 0.0:
            raise ValueError('A base deve ser maior que 0')
        self._base = value

        #getter
    @property
    def altura(self):
        return self._altura
    
    # setter
    @altura.setter 
    def altura(self, value):
        if value <= 0.0:
            raise ValueError('A altura deve ser maior que 0')
        self._altura = value

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

retangulo1.base = 1
retangulo1.base = 1
print(retangulo1.base, retangulo1.altura)
