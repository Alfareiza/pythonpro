"""
https://wiki.python.org.br/ExerciciosClasses
11. Classe carro: Implemente uma classe chamada Carro com as seguintes propriedades:
    a. Um veículo tem um certo consumo de combustível (medidos em km / litro) e
    uma certa quantidade de combustível no tanque.
    b. O consumo é especificado no construtor e o nível de combustível inicial é 0.
    c. Forneça um método andar( ) que simule o ato de dirigir o veículo por uma certa distância,
     reduzindo o nível de combustível no tanque de gasolina.
    d. Forneça um método obterGasolina( ), que retorna o nível atual de combustível.
    e. Forneça um método adicionarGasolina( ), para abastecer o tanque. Exemplo de uso:
    meuFusca = Carro(15);           # 15 quilômetros por litro de combustível.
    meuFusca.adicionarGasolina(20); # abastece com 20 litros de combustível.
    meuFusca.andar(100);            # anda 100 quilômetros.
    meuFusca.obterGasolina()        # Imprime o combustível que resta no tanque.
    >>> meucarro = Carro(15)
    >>> meucarro.adicionarGasolina(20)
    >>> meucarro.andar(100)
    >>> meucarro.obterGasolina()
    13.33
    >>> otrocarro = Carro(7)
    >>> otrocarro.adicionarGasolina(20)
    >>> otrocarro.andar(100)
    >>> otrocarro.obterGasolina()
    5.71
"""


class Carro():
    def __init__(self, km_by_ltr):
        self.km_by_ltr = km_by_ltr
        self.combustivel_tanque = 0

    def adicionarGasolina(self, quant_gas):
        """
        Adiciona gasolina ao carro
        """
        self.combustivel_tanque += quant_gas

    def andar(self, distancia):
        """
        Após o Veículo andar por uma certa distância, reduz o nível de combustível no tanque de gasolina.
        """
        consumo = distancia/self.km_by_ltr
        combustivelTemp = self.combustivel_tanque - round(consumo, 2)
        self.combustivel_tanque = round(combustivelTemp, 2)

    def obterGasolina(self):
        """
         Retorna o nível atual de combustível.
        """
        print(self.combustivel_tanque)
