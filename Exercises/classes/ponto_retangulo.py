"""
https://wiki.python.org.br/ExerciciosClasses
9. Faça um programa completo utilizando funções e classes que:
    a. Possua uma classe chamada Ponto, com os atributos x e y.
    b. Possua uma classe chamada Retangulo, com os atributos largura e altura.
    c. Possua uma função para imprimir os valores da classe Ponto
    d. Possua uma função para encontrar o centro de um Retângulo.
    d. Você deve criar alguns objetos da classe Retangulo.
    e. Cada objeto deve ter um vértice de partida, por exemplo, o vértice inferior esquerdo
    do retângulo, que deve ser um objeto da classe Ponto.
    f. A função para encontrar o centro do retângulo deve retornar o valor para um objeto
     do tipo ponto que indique os valores de x e y para o centro do objeto.
    g. O valor do centro do objeto deve ser mostrado na tela
    i. Crie um menu para alterar os valores do retângulo e imprimir o centro deste retângulo.
"""


class Ponto():
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def read_atributos(self):
        return self.__dict__


class Retangulo():
    def __init__(self, altura, largura, posicao: Ponto):
        self.altura = altura
        self.largura = largura
        self.posicao = posicao

    def center_retangulo(self):
        if self.altura > 0 and self.largura > 0:
            centro = Ponto(self.posicao.x + (self.altura/2), self.posicao.y + (self.largura/2))
            return centro.read_atributos()
        else:
            return 'Não é possível calcular o centro do retangulo'


if __name__ == '__main__':
    meu_punto = Ponto(50, 50)
    print(meu_punto.read_atributos())

    print(9 * '======')
    retangulo0 = Retangulo(10, 20, meu_punto)
    print(f"Dimensões do retángulo: altura={retangulo0.altura}, largura={retangulo0.largura}")
    print(f"Centro do retángulo: {retangulo0.center_retangulo()}")

    print(9 * '======')
    meu_punto = Ponto(1920, 0)
    retangulo1 = Retangulo(854, 480, meu_punto)
    print(f"Retángulo ubicado em {meu_punto.read_atributos()}")
    print(f"Dimensões do retángulo: altura={retangulo1.altura}, largura={retangulo1.largura}")
    print(f"Centro do retángulo: {retangulo1.center_retangulo()}")

    print(9 * '======')
    meu_punto = Ponto(1920, 0)
    largura = input('Digite a largura do retángulo : ')
    altura = input('Digite a altura do retángulo : ')
    retangulo1 = Retangulo(int(altura), int(largura), meu_punto)
    print(f"Retángulo ubicado em {meu_punto.read_atributos()}")
    print(f"Dimensões do retángulo: altura={retangulo1.altura}, largura={retangulo1.largura}")
    print(f"Centro do retángulo: {retangulo1.center_retangulo()}")
