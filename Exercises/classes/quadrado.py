"""
https://wiki.python.org.br/ExerciciosClasses
2. Classe Quadrado: Crie uma classe que modele um quadrado:
            Atributos: Tamanho do lado
            Métodos: Mudar valor do Lado, Retornar valor do Lado e calcular Área;
    >>> meu_quadrado = Quadrado(5)
    >>> meu_quadrado.get_valor_lado()
    5
    >>> meu_quadrado.set_valor_lado(10)
    >>> meu_quadrado.get_valor_lado()
    10
    >>> meu_quadrado.calc_area()
    100
"""


class Quadrado():
    def __init__(self, tamanho_do_lado=0):
        self.tamanho_do_lado = tamanho_do_lado

    def get_valor_lado(self):
        print(self.tamanho_do_lado)

    def set_valor_lado(self, num):
        self.tamanho_do_lado = num

    def calc_area(self):
        area = self.tamanho_do_lado ** 2
        return area
