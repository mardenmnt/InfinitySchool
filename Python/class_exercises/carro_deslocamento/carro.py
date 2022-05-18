"""
Implemente uma classe chamada Carro com as seguintes propriedades:

— Um veículo tem um certo consumo de combustível (medidos em km / litro) e uma certa quantidade de combustível no tanque.
— O consumo é especificado no construtor e o nível de combustível inicial é 0.
— Forneça um método andar( ) que simule o ato de dirigir o veículo por uma certa distância, reduzindo o nível de combustível no tanque de gasolina.
— Forneça um método obterGasolina( ), que retorna o nível atual de combustível.
— Forneça um método adicionarGasolina( ), para abastecer o tanque.

Exemplo de uso:

meuFusca = Carro(15);           # 15 quilômetros por litro de combustível.
meuFusca.adicionarGasolina(20); # abastece com 20 litros de combustível.
meuFusca.andar(100);            # anda 100 quilômetros.
meuFusca.obterGasolina()        # Imprime o combustível que resta no tanque.
"""


class Carro:
    def __init__(self, consumo):
        self.consumo = consumo
        self.qtd_combustivel = 0

    def andar(self, distancia):
        if self.qtd_combustivel <= 0:
            return f'QTD de combustível insuficiente! Abasteça o veículo'
        else:
            consumo = distancia / self.consumo
            self.qtd_combustivel -= consumo

            if self.qtd_combustivel <= 0:
                return f'QTD de combustível insuficiente para {distancia}Km'
            else:
                return f'Iniciando deslocamento...'

    @property
    def obter_gasolina(self):
        return f'Total de Gasolina: {self.qtd_combustivel}L'

    def adicionar_gasolina(self, litros):
        self.qtd_combustivel += litros
        return f'Abastecendo {litros}L ...'
