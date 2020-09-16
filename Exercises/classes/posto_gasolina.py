"""
https://wiki.python.org.br/ExerciciosClasses
10. Classe Bomba de Combustível: Faça um programa completo utilizando classes e métodos que:
    a. Possua uma classe chamada bombaCombustível, com no mínimo esses atributos:
        i. tipoCombustivel.
        ii. valorLitro
        iii. quantidadeCombustivel
    b. Possua no mínimo esses métodos:
        i. abastecerPorValor( ) – método onde é informado o valor a ser abastecido e
            mostra a quantidade de litros que foi colocada no veículo
        ii. abastecerPorLitro( ) – método onde é informado a quantidade em litros de
            combustível e mostra o valor a ser pago pelo cliente.
        iii. alterarValor( ) – altera o valor do litro do combustível.
        iv. alterarCombustivel( ) – altera o tipo do combustível.
        v. alterarQuantidadeCombustivel( ) – altera a quantidade de combustível restante na bomba.
    OBS: Sempre que acontecer um abastecimento é necessário atualizar a quantidade de
        combustível total na bomba.

    >>> posto1 = bombaCombustível('Etanol', 2.6, 1000)
    >>> posto1.tipoCombustivel
    'Etanol'
    >>> posto1.valorLitro
    2.6
    >>> posto1.quantidadeCombustivel
    1000
    >>> posto1.abastecerPorValor(50)
    19.23
    >>> posto1.quantidadeCombustivel
    980.77
    >>> posto1.abastecerPorLitro(10)
    26.0
    >>> posto1.quantidadeCombustivel
    970.77
    >>> posto1.alterarValor(2.9)
    >>> posto1.abastecerPorValor(50)
    17.24
    >>> posto1.abastecerPorLitro(15)
    43.5
    >>> posto1.quantidadeCombustivel
    938.53
"""


class bombaCombustível():
    def __init__(self, tipoCombustivel, valorLitro, quantidadeCombustivel):
        self.tipoCombustivel = tipoCombustivel
        self.valorLitro = valorLitro
        self.quantidadeCombustivel = quantidadeCombustivel

    def abastecerPorValor(self, valor_reais_abastecer):
        """
        É informado o valor em reais a ser abastecido e mostra a quantidade de
        litros que foi colocada no veículo.
        """
        valor_litros_abastecer = valor_reais_abastecer / self.valorLitro
        valor_litros_abastecer = round(valor_litros_abastecer, 2)
        self.quantidadeCombustivel -= valor_litros_abastecer
        return valor_litros_abastecer

    def abastecerPorLitro(self, quant_ltrs):
        """
        É informado a quantidade em litros de combustível e mostra o valor
        a ser pago pelo cliente.
        """
        self.quantidadeCombustivel -= quant_ltrs
        return quant_ltrs * self.valorLitro

    def alterarValor(self, new_value):
        """
        Altera o valor do litro do combustível.
        """
        self.valorLitro = new_value

    def alterarCombustivel(self, new_tipoCombustivel):
        """
        Altera o tipo do combustível.
        """
        self.tipoCombustivel = new_tipoCombustivel

    def alterarQuantidadeCombustivel(self, new_quantidaCombustivel):
        """
        Altera a quantidade de combustível restante na bomba.
        """
        self.quantidadeCombustivel = new_quantidaCombustivel
