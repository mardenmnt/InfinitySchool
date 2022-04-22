"""
Crie programa que calcule o custo final de um veículo,
tendo como entrada o valor de fábrica do veículo.
Tendo como base que a taxa do distribuidor é de 28% e tenha 45% de impostos
"""

custo_fabrica = float(input('Informe o custo de fábrica do carro: '))

distribuidor = 0.28 * custo_fabrica
impostos = 0.45 * custo_fabrica

print('O custo final do carro foi de:', custo_fabrica + distribuidor + impostos, 'reais')
