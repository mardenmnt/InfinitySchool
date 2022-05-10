"""
Faça um Programa que peça um número e informe se o número é inteiro ou decimal.
"""

num = float((input('Informe numero: ')).replace(',', '.'))

if num % 1 == 0:
    print('Inteiro')
else:
    print('Decimal')
