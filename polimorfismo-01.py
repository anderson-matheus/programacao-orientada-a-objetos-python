import math


class Forma():
    def __init__(self):
        """
        Método Construtor
        """
        print('Construtor da forma')

    def area(self):
        """
        Método que calcula a área
        """
        print('Área da forma')

    def perimetro(self):
        """
        Método que calcula o perímetro
        """
        print('Perímetro da forma')

    def descricao(self):
        """
        Método que retorna a descrição da Forma
        """
        print('Descrição da forma')


class Quadrado(Forma):
    def __init__(self, lado):
        """
        Construtor que inicializa com o valor do lado do quadrado
        """
        self.lado = lado

    def area(self):
        return self.lado ** 2

    def perimetro(self):
        return self.lado * 4


class Circulo(Forma):
    def __init__(self, raio):
        self.raio = raio

    def area(self):
        return math.pi * self.raio ** 2

    def perimetro(self):
        return 2 * math.pi * self.raio

    def descricao(self):
        return 'Descrição do círculo'


quad = Quadrado(2)
print('Quadrado')
print('Área: %d' % quad.area())
print('Perímetro:: %d' % quad.perimetro())

print('\n')

circulo = Circulo(3)
print('Círculo')
print('Área: %f' % circulo.area())
print('Perímetro: %f' % circulo.perimetro())
print(circulo.descricao())
