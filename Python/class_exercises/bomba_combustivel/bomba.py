"""
Faça um programa completo utilizando classes e métodos que:

Possua uma classe chamada bombaCombustível, com no mínimo esses atributos:
tipoCombustivel.
valorLitro
quantidadeCombustivel

Possua no mínimo esses métodos:
abastecerPorValor( ) – método onde é informado o valor a ser abastecido e mostra a quantidade de litros que foi colocada no veículo
abastecerPorLitro( ) – método onde é informado a quantidade em litros de combustível e mostra o valor a ser pago pelo cliente.
alterarValor( ) – altera o valor do litro do combustível.
alterarCombustivel( ) – altera o tipo do combustível.
alterarQuantidadeCombustivel( ) – altera a quantidade de combustível restante na bomba.
OBS: Sempre que acontecer um abastecimento é necessário atualizar a quantidade de combustível total na bomba
"""


class BombaCombustivel:
    def __init__(self, tipo_combustivel, valor_litro, qtd_combustivel):
        self.tipo_combustivel = tipo_combustivel
        self.valor_litro = valor_litro
        self.qtd_combustivel = qtd_combustivel

    def abastecer_valor(self, valor):
        total_litros = valor / self.valor_litro
        self.qtd_combustivel -= total_litros
        return f'{total_litros} L'

    def abastecer_litro(self, litros):
        self.qtd_combustivel -= litros
        valor = self.valor_litro * litros
        return f'Total a pagar: R$ {valor:.2f}'

    def alterar_valor_litro(self, valor):
        self.valor_litro = valor
        return f'Novo valor de {self.tipo_combustivel} é R${valor}'

    def alterar_tipo_combustivel(self, tipo):
        self.tipo_combustivel = tipo
        return 'Tipo de combustível alterado com sucesso!'

    def alterar_qtd_combustivel(self, qtd):
        self.qtd_combustivel = qtd
        return f'Nova QTD de {self.tipo_combustivel} é {self.qtd_combustivel}L'
