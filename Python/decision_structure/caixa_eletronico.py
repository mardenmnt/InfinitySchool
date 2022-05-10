"""
Faça um Programa para um caixa eletrônico.
O programa deverá perguntar ao usuário a valor do saque e depois informar quantas notas de cada valor serão fornecidas.
As notas disponíveis serão as de 1, 5, 10, 50 e 100 reais. O valor mínimo é de 10 reais e o máximo de 600 reais.
O programa não deve se preocupar com a quantidade de notas existentes na máquina.

Exemplo 1: Para sacar 256 reais, o programa fornece duas notas de 100, uma nota de 50, uma nota de 5 e uma nota de 1;
Exemplo 2: Para sacar 399 reais, o programa fornece três notas de 100, uma nota de 50, quatro notas de 10,
uma nota de 5 e quatro notas de 1.
"""

saque = int(input('\nInforme o valor que deseja sacar: ').replace(',', '.'))

while saque < 10 or saque > 600:
    print('Fora dos limites de saque!')
    print('Por favor informe um valor de saque entre 10 e 600 reais')
    saque = int(input('Informe o valor que deseja sacar: '))

# número de notas de 100
cem = int(saque / 100)
# atualizando valor saque, retirando quantidade de cédulas de 100
saque = saque - (cem * 100)
# número de notas de 50
cinquenta = int(saque / 50)
# atualizando valor saque, retirando quantidade de cédulas de 50
saque = saque - cinquenta * 50
# número de notas de 10
dez = int(saque / 10)
# atualizando valor saque, retirando quantidade de cédulas de 10
saque = saque - (dez * 10)
# número de notas de 5
cinco = int(saque / 5)
# atualizando valor saque, retirando quantidade de cédulas de 5
saque = saque - (cinco * 5)
# número de notas de 1
um = saque

print(f'{cem} notas de 100\n'
      f'{cinquenta} notas de 50\n'
      f'{dez} notas de 10\n'
      f'{cinco} notas de 5\n'
      f'{um} notas de 1')
